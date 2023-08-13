# -*- encoding: utf-8 -*-

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
    """
    The context maker function is used to remake the incoming context to Json format

    Args:
        context_in (dataset): The sorted data set of model

    Returns:
        _type_: Json formatted string
    """
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
    """
    The Index view of the system

    Args:
        request (httprequest): HTTP request for index html file

    Returns:
        HttpResponse: The page response
    """
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
# @allowed_users(allowed_roles=['manager']) #decorator for testing
def pages(request):
    """
    The page request and error response handling function

    Args:
        request (httprequest): HTTP request for html file

    Returns:
        HttpResponse: The page response
    """
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
    """
    The Customer page template view
    
    Args:
        TemplateView (TemplateView): The Template view geneic class
    """
    template_name = 'customers.html'

class SupplierTemplate(TemplateView):
    """
    The Supplier page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class
    """
    template_name = 'suppliers.html'

class SettingsTemplate(TemplateView):
    """
    The Setting page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class
    """
    template_name = 'settings.html'

class RegisterTemplate(TemplateView):
    """
    The User Registeration page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class
    """
    template_name = 'accounts/register.html'

class MaterialsTemplate(TemplateView):
    """
    The Material page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class
    """
    template_name = 'materials.html'

    def get_context_data(self, **kwargs):
        """
        Overwritting the get_context_data method for handing sidebar UI
        | segment : 'materials'

        Returns:
            context: http response context
        """
        context = super().get_context_data(**kwargs)
        context['segment'] = 'materials'
        return context

class ShellsTemplate(TemplateView):
    """
    The shell page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class

    """
    template_name = 'shells.html'

    def get_context_data(self, **kwargs):
        """
        Overwritting the get_context_data method for handing sidebar UI
        | segment : 'shells'

        Returns:
            context: http response context
        """
        context = super().get_context_data(**kwargs)
        context['segment'] = 'shells'
        return context

class PurchaseOrderTemplate(TemplateView):
    """
    The Purchase Order page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class

    """
    template_name = 'purchase-order.html'

    def get_context_data(self, **kwargs):
        """
        Overwritting the get_context_data method for handing sidebar UI
        | segment : 'purchase-order'

        Returns:
            context: http response context
        """
        context = super().get_context_data(**kwargs)
        context['segment'] = 'purchase-order'
        return context

class ItemsTemplate(TemplateView):
    """
    The Stock Items page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class

    """
    template_name = 'items.html'

    def get_context_data(self, **kwargs):
        """
        Overwritting the get_context_data method for handing sidebar UI
        | segment : 'items'

        Returns:
            context: http response context
        """
        context = super().get_context_data(**kwargs)
        context['segment'] = 'items'
        return context

class SalesOrderTemplate(TemplateView):
    """
    The Sales Order page templatet view

    Args:
        TemplateView (TemplateView): The Template view geneic class

    """
    template_name = 'sales-order.html'

    def get_context_data(self, **kwargs):
        """
        Overwritting the get_context_data method for handing sidebar UI
        | segment : 'sales-order'

        Returns:
            context: http response context
        """
        context = super().get_context_data(**kwargs)
        context['segment'] = 'sales-order'
        return context

class PreSalesOrderTemplate(TemplateView):
    """
    The Pre Sales Order page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class

    """
    template_name = 'pre-sales-order.html'

    def get_context_data(self, **kwargs):
        """
        Overwritting the get_context_data method for handing sidebar UI
        | segment : 'pre-sale-order'

        Returns:
            context: http response context
        """
        context = super().get_context_data(**kwargs)
        context['segment'] = 'pre-sale-order'
        return context

class QuotationTemplate(TemplateView):
    """
    The Quuatation page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class

    """
    template_name = 'quatation.html'

    def get_context_data(self, **kwargs):
        """
        Overwritting the get_context_data method for handing sidebar UI
        | segment : 'quatation'

        Returns:
            context: http response context
        """
        context = super().get_context_data(**kwargs)
        context['segment'] = 'quatation'
        return context

class BillingTemplate(TemplateView):
    """
    The Billing page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class

    """
    template_name = 'billing.html'

    def get_context_data(self, **kwargs):
        """
        Overwritting the get_context_data method for handing sidebar UI
        | segment : 'billing'

        Returns:
            context: http response context
        """
        context = super().get_context_data(**kwargs)
        context['segment'] = 'billing'
        return context
    
class DashboardTemplate(TemplateView):
    """
    The Dashoard page template view

    Args:
        TemplateView (TemplateView): The Template view geneic class

    """
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        """
        Overwritting the get_context_data method for handing sidebar UI
        | segment : 'dashboard'

        Returns:
            context: http response context
        """
        context = super().get_context_data(**kwargs)
        context['segment'] = 'dashboard'
        return context
    