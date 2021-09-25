from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize

from .models import Customer
from .form import CustomerRegister, CustomerUpdate
from .filters import CustomerFilter

from app.views import context_packer
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.urls import reverse_lazy
from django.views import generic

from django.core.paginator import Paginator


from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

# customer list wth pagination
class CustomersList(generic.ListView):
    model = Customer
    paginate_by = 2
    context_object_name = "customers"
    template_name = 'pages/customers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['customers'] = Customer.objects.all()
        context['filter'] = CustomerFilter()
        
        return context

# customer Details
class CustomerDetails(generic.detail.DetailView):
    model = Customer
    context_object_name = "c_customer"
    template_name = 'pages/customers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CustomerFilter(self.request.GET, queryset=Customer.objects.all())
        
        customer_paginator = Paginator(context['filter'].qs, 1)
        page_number = self.request.GET.get('page')

        if type(page_number) is str:
            page_number = int(page_number)
        else:
            page_number = 1

        context['page_obj'] = customer_paginator.get_page(page_number)
        context['customers'] = customer_paginator.page(page_number)
        print (context['customers'])

        return context


# Customer Create
class CustomerCreateView(BSModalCreateView):
    template_name = 'pages/modals/customer-create.html'
    form_class = CustomerRegister
    success_message = 'Success: New Customer was created.'
    success_url = reverse_lazy('/pages/customers.html')

# Customer Update
class CustomerUpdateView(BSModalUpdateView):
    model = Customer
    template_name = 'pages/modals/customer-update.html'
    form_class = CustomerUpdate
    success_message = 'Success: Selected Customer was updated.'
    success_url = reverse_lazy('/pages/customers.html')

# Customer Delete
class CustomerDeleteView(BSModalDeleteView):
    model = Customer
    template_name = 'pages/modals/customer-delete.html'
    success_message = 'Success: Selected Customer was deleted.'
    success_url = reverse_lazy('/pages/customers.html')


