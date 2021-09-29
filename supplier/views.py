from django.contrib.auth.decorators import login_required
from .models import Supplier
from .forms import SupplierRegister, SupplierUpdate
from .filters import SupplierFilter

from django.urls import reverse_lazy
from django.views import generic

from django.core.paginator import Paginator
from django.db.models import Sum

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)


# supplier list with pagination
class SuppliersList(generic.ListView):
    model = Supplier
    paginate_by = 7
    context_object_name = "suppliers"
    template_name = 'pages/suppliers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_orders'] = Supplier.objects.aggregate(Sum('po_count'))
        context['supplier_count'] = Supplier.objects.count()
        context['num_of_objects'] = Supplier.objects.count()
        context['c_supplier'] = Supplier.objects.first()
        context['filter'] = SupplierFilter(self.request.GET, queryset=Supplier.objects.all())
        context['segment'] = 'suppliers'
        return context

# supplier Details
class SupplierDetails(generic.detail.DetailView):
    model = Supplier
    context_object_name = "c_supplier"
    template_name = 'pages/suppliers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SupplierFilter(self.request.GET, queryset=Supplier.objects.all())
        
        supplier_paginator = Paginator(context['filter'].qs, 7)
        page_number = self.request.GET.get('page')

        if type(page_number) is str:
            page_number = int(page_number)
        else:
            page_number = 1

        context['supplier_count'] = Supplier.objects.count()
        context['total_orders'] = Supplier.objects.aggregate(Sum('po_count'))
        context['page_obj'] = supplier_paginator.get_page(page_number)
        context['suppliers'] = supplier_paginator.page(page_number)
        context['num_of_objects'] = supplier_paginator.count
        context['segment'] = 'suppliers'

        return context

# Customer Create
class SupplierCreateView(BSModalCreateView):
    template_name = 'pages/modals/supplier/supplier-create.html'
    form_class = SupplierRegister
    success_message = 'Success: New Supplier was created.'
    success_url = reverse_lazy('suppliers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generated_id'] = Supplier.supplier_id()
        return context

# Customer Update
class SupplierUpdateView(BSModalUpdateView):
    model = Supplier
    template_name = 'pages/modals/supplier/supplier-update.html'
    form_class = SupplierUpdate
    success_message = 'Success: Selected Supplier was updated.'
    success_url = reverse_lazy('suppliers')

# Customer Delete
class SupplierDeleteView(BSModalDeleteView):
    model = Supplier
    template_name = 'pages/modals/supplier/supplier-delete.html'
    success_message = 'Success: Selected Supplier was deleted.'
    success_url = reverse_lazy('suppliers')

