from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .models import PurchaseOrder, CMaterial
from .filters import PurchaseOrderFilter
from .forms import PurchaseOrderForm,  CMaterialForm, CMaterialFormSet, PurchaseOrderStatusForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

# Create your views here.
# purchase order list
class PurchaseOrderList(LoginRequiredMixin, generic.ListView):
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
        context['create'] = 1
        context['segment'] = 'purchase-order'
        return context

# purchase order Details
class PurchaseOrderDetails(LoginRequiredMixin, generic.detail.DetailView):
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
        context['create'] = 0
        return context

# def update_status(request, pk):
#     print ('id : ', pk)
#     po_object = PurchaseOrder.objects.filter(id=pk).first()
#     if po_object.status == 0:
#         po_object.status = 1 # paid for purchase-order
#     elif po_object.status == 1:
#         po_object.status = 2 # received from supplier
#     elif po_object.status == 2:
#         po_object.status = 3 # closed purchase-order
#     elif po_object.status == 3:
#         print('closed')
#     po_object.save()

#     print(po_object)

#     return redirect('/purchase-order/')

def create_po(request):
    context = {}
    # context['filter'] = PurchaseOrderFilter(queryset=PurchaseOrder.objects.all())
    # context['PurchaseOrders'] = context['filter'].qs
    # context['Order'] = PurchaseOrder.objects.all().first()
    # create = 1 for preview window
    context['create'] = 0

    return redirect('/purchase-order/', context)

class po_view(generic.TemplateView):
    template_name = 'documents/purchase-order-doc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            po_id = self.request.path.rsplit('/', 1)[-1]
            context['Order'] = PurchaseOrder.objects.filter(id=po_id)[0]
            context['other_count'] = range(context['Order'].material_ids.count()+1, (10+context['Order'].material_ids.count()) - context['Order'].material_ids.count())
        context['segment'] = 'purchase-order'
        context['user'] = self.request.user

        # create = 1 for preview window
        context['create'] = 1
        return context

# create po view
class PurchaseOrderDocTemplate(LoginRequiredMixin, generic.CreateView):
    template_name = 'documents/purchase-order-doc.html'
    model=PurchaseOrder
    form_class = PurchaseOrderForm
    context_object_name = "PO_form"
    success_url = reverse_lazy('purchase-order-doc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = 0
        context['po_id'] = PurchaseOrder.po_id()
        context['date'] = datetime.datetime.now()
        context['form_set'] = CMaterialFormSet() 

        return context

    def form_valid(self, form):

        if self.request.method == 'POST':
            ctx = self.get_context_data()
            form_set = CMaterialFormSet(self.request.POST or None)
            po_id = PurchaseOrderForm(self.request.POST)
            if po_id.is_valid():
                po_id = po_id.save()

            if form_set.is_valid():
                for form_material in form_set:
                    material = form_material.save(commit=False)
                    if form_material.is_valid() and not material.material_id==None:
                        material.po_id = po_id
                        material.save()
                        po_id.material_ids.add(material)

        return super(PurchaseOrderDocTemplate, self).form_valid(form)

# Purchase Order Update
class StatusUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = PurchaseOrder
    template_name = 'pages/modals/purchase-order/po-info.html'
    form_class  = PurchaseOrderStatusForm
    success_message = 'Success: Selected Purchase Order\' status was updated.'
    success_url = reverse_lazy('purchase-order')

    def post(self, request, *args, **kwargs):
        po_object = PurchaseOrder.objects.filter(id=request.POST.get('id')).first()
        if po_object.status == 0:
            # paid for purchase-order
            po_object.status = 1 
            po_object.paid_date = datetime.datetime.now()

        elif po_object.status == 1:
            # received from supplier
            po_object.status = 2
            po_object.Received_date = datetime.datetime.now()

            for cmaterial in po_object.material_ids.all():
                material = cmaterial.material_id
                material.quatity += cmaterial.quantity
                material.save()
                material.make_stock_status()
                material.save()

        elif po_object.status == 2:
            # closed purchase-order
            po_object.status = 3 
            po_object.closed_date = datetime.datetime.now()
        po_object.save()

        return redirect('/purchase-order/')


# Purchase Order Delete
class PurchaseOrderDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = PurchaseOrder
    template_name = 'pages/modals/purchase-order/po-delete.html'
    success_message = 'Success: Selected Purchase Order was deleted.'
    success_url = reverse_lazy('purchase-order')