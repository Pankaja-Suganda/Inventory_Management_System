# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from authentication.decorator import allowed_users
from authentication.models import BaseUser
from authentication.forms import ProfileUpdate, UserPasswordUpdate, UserUpdatePer
from customer.filters import CustomerFilter
from customer.models import Customer
from customer.form import CustomerRegister

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
# @allowed_users(allowed_roles=['manager']) #decorator for testing
def pages(request):
    context = {}
    context['user'] = request.user
    context['users'] = BaseUser.objects.all()
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.

    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template.replace('.html','')

        # for settings section
        if context['segment'] == 'settings':
            context['form'] = ProfileUpdate(instance=request.user)
            context['form_reset'] = UserPasswordUpdate()
            context['select'] = 'account-general'
            context['form_per'] = UserUpdatePer()
        
        # for customer section
        elif context['segment'] == 'customers':
            if request.POST:
                context['customers'] = Customer.objects.all()
                context['filter'] = CustomerFilter()
                context['customer_reg'] = CustomerRegister()
            else:
                customers = Customer.objects.all()
                cus_filter = CustomerFilter(request.GET, queryset=customers)
                context['customers'] = cus_filter.qs
                context['filter'] = cus_filter
                context['customer_reg'] = CustomerRegister()
            
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
