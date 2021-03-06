from django.contrib.auth.decorators import login_required
from .models import Customer
from .form import CustomerRegister, CustomerUpdate
from .filters import CustomerFilter

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.core import serializers
import json

from django.core.paginator import Paginator


from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

# customer list wth pagination
class CustomersList(LoginRequiredMixin, generic.ListView):
    model = Customer
    paginate_by = 7
    context_object_name = "customers"
    template_name = 'pages/customers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = Customer.objects.count()
        context['num_of_objects'] = count
        if count >= 0:
            context['c_customer'] = Customer.objects.first()
        else:
            context['c_customer'] = None

        context['filter'] = CustomerFilter(self.request.GET, queryset=Customer.objects.all())
        context['segment'] = 'customers'
        if not count == 0:
            context['Active_customers'] = { 'count': Customer.objects.filter(status=0).count(), 
                                            'persentage': "{:.2f}".format(round((Customer.objects.filter(status=0).count() / count)*100, 2))
                                            }
            context['Expired_customers'] = { 'count': Customer.objects.filter(status=1).count(), 
                                            'persentage': "{:.2f}".format(round((Customer.objects.filter(status=1).count() / count)*100, 2))
                                            }
            context['Suspended_customers'] = { 'count': Customer.objects.filter(status=2).count(), 
                                            'persentage': "{:.2f}".format(round((Customer.objects.filter(status=2).count() / count)*100, 2))
                                            }
        return context

# customer Details
class CustomerDetails(LoginRequiredMixin, generic.detail.DetailView):
    model = Customer
    context_object_name = "c_customer"
    template_name = 'pages/customers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CustomerFilter(self.request.GET, queryset=Customer.objects.all())
        
        customer_paginator = Paginator(context['filter'].qs, 7)
        page_number = self.request.GET.get('page')

        if type(page_number) is str:
            page_number = int(page_number)
        else:
            page_number = 1

        count = Customer.objects.count()
        context['page_obj'] = customer_paginator.get_page(page_number)
        context['customers'] = customer_paginator.page(page_number)
        context['num_of_objects'] = count
        context['segment'] = 'customers'
        if not count == 0:
            context['Active_customers'] = { 'count': Customer.objects.filter(status=0).count(), 
                                            'persentage': "{:.2f}".format(round((Customer.objects.filter(status=0).count() / count)*100, 2))
                                            }
            context['Expired_customers'] = { 'count': Customer.objects.filter(status=1).count(), 
                                            'persentage': "{:.2f}".format(round((Customer.objects.filter(status=1).count() / count)*100, 2))
                                            }
            context['Suspended_customers'] = { 'count': Customer.objects.filter(status=2).count(), 
                                            'persentage': "{:.2f}".format(round((Customer.objects.filter(status=2).count() / count)*100, 2))
                                            }

        return context


# Customer Create
class CustomerCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'pages/modals/customer/customer-create.html'
    form_class = CustomerRegister
    success_message = 'Success: New Customer was created.'
    success_url = reverse_lazy('customers')
    failure_url = reverse_lazy('customers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generated_id'] = Customer.customer_id()
        return context

# Customer Update
class CustomerUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Customer
    template_name = 'pages/modals/customer/customer-update.html'
    form_class = CustomerUpdate
    success_message = 'Success: Selected Customer was updated.'
    success_url = reverse_lazy('customers')
    failure_url = reverse_lazy('customers')

# Customer Delete
class CustomerDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Customer
    template_name = 'pages/modals/customer/customer-delete.html'
    success_message = 'Success: Selected Customer was deleted.'
    success_url = reverse_lazy('customers')
    failure_url = reverse_lazy('customers')

# customer Details for documents
def CustomerDetailsAdd(request, pk):
    customer = Customer.objects.get(pk=pk)
    return HttpResponse(serializers.serialize("json", [customer]), content_type="application/json")


