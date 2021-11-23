# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django import template
from django.core.serializers import deserialize
import datetime

# from authentication application
from authentication.decorator import allowed_users
from authentication.models import BaseUser
from authentication.forms import ProfileUpdate, UserPasswordUpdate, UserUpdatePer

# from customer Application
from customer.filters import CustomerFilter
from customer.models import Customer
from customer.form import CustomerRegister

# from Supplier Application
from supplier.filters import SupplierFilter
from supplier.models import Supplier
from supplier.forms import SupplierRegister

# from purchaseorder Application
from purchase_order.models import PurchaseOrder

#  for packing the model pass one view to another
# def context_packer(model, name, id):
#     if not model == None:
#         context = {
#                 "model" : model.__name__, 
#                 "id" : id,
#                 "name": name
#             }
#     else:
#         context = {
#                 "model" : None, 
#                 "id" : id,
#                 "name": name
#             }

#     return context

# for remaking the model from passed data from previous view
def context_maker(context_in):
    context = {}
    for value in context_in.values():
        if value['model'] == Customer.__name__:
            context[value['name']] = Customer.objects.get(id=value['id'])
        elif value['model'] == Supplier.__name__:
            context[value['name']] = Supplier.objects.get(id=value['id'])
        elif value['model'] == None:
            context[value['name']] = value['id']

    return context


@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
# @allowed_users(allowed_roles=['manager']) #decorator for testing
def pages(request):

    if not request.session.get("context")==None:
        # context = context_maker(request.session.get("context"))
        print ('context : ')
    else:
        context = {}

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.

    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template.replace('.html','')

        print('load : ', load_template)
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

class CustomerTemplate(TemplateView):
    template_name = 'customers.html'

class SupplierTemplate(TemplateView):
    template_name = 'suppliers.html'

class SettingsTemplate(TemplateView):
    template_name = 'settings.html'

class RegisterTemplate(TemplateView):
    template_name = 'accounts/register.html'

class MaterialsTemplate(TemplateView):
    template_name = 'materials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'materials'
        return context

class ShellsTemplate(TemplateView):
    template_name = 'shells.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'shells'
        return context

class PurchaseOrderTemplate(TemplateView):
    template_name = 'purchase-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'purchase-order'
        return context

class ItemsTemplate(TemplateView):
    template_name = 'items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'items'
        return context

class SalesOrderTemplate(TemplateView):
    template_name = 'sales-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'sales-order'
        return context

class PreSalesOrderTemplate(TemplateView):
    template_name = 'pre-sales-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'pre-sale-order'
        return context

class QuotationTemplate(TemplateView):
    template_name = 'quatation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'quatation'
        return context

class BillingTemplate(TemplateView):
    template_name = 'billing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'billing'
        return context
    