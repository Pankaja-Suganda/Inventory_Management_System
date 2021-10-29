from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import PurchaseOrder
from .filters import PurchaseOrderFilter

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

# Create your views here.
# po Create view
# class SupplierCreateView(BSModalCreateView):
#     template_name = 'pages/modals/supplier/supplier-create.html'
#     form_class = SupplierRegister
#     success_message = 'Success: New Supplier was created.'
#     success_url = reverse_lazy('suppliers')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['generated_id'] = PurchaseOrder.po_id()
#         return context
        
# purchase order list
class PurchaseOrderList(generic.ListView):
    model = PurchaseOrder
    context_object_name = "PurchaseOrders"
    template_name = 'pages/purchase-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PurchaseOrderFilter(self.request.GET, queryset=PurchaseOrder.objects.all())
        context['PurchaseOrders'] = context['filter'].qs
        context['issued'] = PurchaseOrder.objects.filter(status=0).count()
        context['paid'] = PurchaseOrder.objects.filter(status=1).count()
        context['received'] = PurchaseOrder.objects.filter(status=2).count()
        context['closed'] = PurchaseOrder.objects.filter(status=3).count()
        context['segment'] = 'purchase-order'
        return context

# purchase order Details
class PurchaseOrderDetails(generic.detail.DetailView):
    model = PurchaseOrder
    context_object_name = "PO_selected"
    template_name = 'pages/purchase-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PurchaseOrderFilter(self.request.GET, queryset=PurchaseOrder.objects.all())
        context['PurchaseOrders'] = context['filter'].qs
        context['issued'] = PurchaseOrder.objects.filter(status=0).count()
        context['paid'] = PurchaseOrder.objects.filter(status=1).count()
        context['received'] = PurchaseOrder.objects.filter(status=2).count()
        context['closed'] = PurchaseOrder.objects.filter(status=3).count()
        context['segment'] = 'purchase-order'
        return context

def update_status(request, id):
    print ('id : ', id)
    return redirect('pages/purchase-order.html')