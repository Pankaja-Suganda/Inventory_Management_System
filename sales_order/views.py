from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .models import SalesOrder, CProduct
from .filters import SalesOrderFilter
from .forms import SalesOrderForm,  CProductForm, CProductlFormSet, SalesOrderStatusForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from invoice.models import Invoice
from django.http import HttpResponse
from django.core import serializers

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

SALES_ORDER_MODE = 1
PRE_SALES_ORDER_MODE = 2

# Create your views here.
# sales order list
class SalesOrderList(LoginRequiredMixin, generic.ListView):
    model = SalesOrder
    context_object_name = "SalesOrders"
    template_name = 'pages/sales-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SalesOrderFilter(self.request.GET, queryset=SalesOrder.objects.all())
        context['SalesOrders'] = context['filter'].qs
        context['total'] = SalesOrder.objects.all().count()
        context['issued'] = SalesOrder.objects.filter(status=0).count()
        context['produced'] = SalesOrder.objects.filter(status=1).count()
        context['delivered'] = SalesOrder.objects.filter(status=2).count()
        context['returned'] = SalesOrder.objects.filter(status=3).count()
        context['closed'] = SalesOrder.objects.filter(status=4).count()
        context['create'] = 1
        context['segment'] = 'sales-order'
        return context

# sales order Details
class SalesOrderDetails(LoginRequiredMixin, generic.detail.DetailView):
    model = SalesOrder
    context_object_name = "SO_selected"
    template_name = 'pages/sales-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SalesOrderFilter(self.request.GET, queryset=SalesOrder.objects.all())
        context['SalesOrders'] = context['filter'].qs
        context['total'] = SalesOrder.objects.all().count()
        context['issued'] = SalesOrder.objects.filter(status=0).count()
        context['produced'] = SalesOrder.objects.filter(status=1).count()
        context['delivered'] = SalesOrder.objects.filter(status=2).count()
        context['returned'] = SalesOrder.objects.filter(status=3).count()
        context['closed'] = SalesOrder.objects.filter(status=4).count()
        context['segment'] = 'sales-order'
        context['create'] = 0
        return context

# create so view
class SalesOrderDocTemplate(LoginRequiredMixin, generic.CreateView):
    template_name = 'documents/sales-order-doc.html'
    model=SalesOrder
    form_class = SalesOrderForm
    context_object_name = "SO_form"
    success_url = reverse_lazy('sales-order-doc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = 0
        context['so_id'] = SalesOrder.so_id()
        context['date'] = datetime.datetime.now()
        context['form_set'] = CProductlFormSet() 

        return context

    def form_valid(self, form):

        if self.request.method == 'POST':
            ctx = self.get_context_data()
            form_set = CProductlFormSet(self.request.POST or None)
            so_id = SalesOrderForm(self.request.POST)
            if so_id.is_valid():
                so_id = so_id.save()

            if form_set.is_valid():
                for form_product in form_set:
                    product = form_product.save(commit=False)
                    if form_product.is_valid() and not product.product_id==None and not product.quantity==0:
                        product.so_id = so_id
                        product.save()
                        so_id.product_ids.add(product)

        return super(SalesOrderDocTemplate, self).form_valid(form)

# creating so
def create_so(request):
    context = {}
    context['create'] = 0

    return redirect('/sales-order/', context)

# preview the generated SO
class so_view(generic.TemplateView):
    template_name = 'documents/sales-order-doc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            po_id = self.request.path.rsplit('/', 1)[-1]
            context['Order'] = SalesOrder.objects.filter(id=po_id)[0]
            context['other_count'] = range(context['Order'].product_ids.count()+1, (10+context['Order'].product_ids.count()) - context['Order'].product_ids.count())
        context['segment'] = 'sales-order'
        context['user'] = self.request.user

        # create = 1 for preview window
        context['create'] = 1
        return context

# Sales Order Update
class StatusUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = SalesOrder
    template_name = 'pages/modals/sales-order/so-info.html'
    form_class  = SalesOrderStatusForm
    success_message = 'Success: Selected Sales Order\' status was updated.'
    success_url = reverse_lazy('sales-order')

    def post(self, request, *args, **kwargs):

        so_object = SalesOrder.objects.filter(id=request.POST.get('id')).first()
        returned = int(request.path.split('/')[-1])

        if so_object.status == 0:
            # finishing production for sales-order
            so_object.status = 1 
            so_object.Produced_date = datetime.datetime.now()

            for cproduct in so_object.product_ids.all():
                product = cproduct.product_id
                product.quatity += cproduct.quantity
                product.save()
                product.make_stock_status()
                product.save()

        elif so_object.status == 1:
            # Send to customer
            so_object.status = 2
            so_object.Sended_date = datetime.datetime.now()

            for cproduct in so_object.product_ids.all():
                product = cproduct.product_id
                product.quatity -= cproduct.quantity
                product.save()
                product.make_stock_status()
                product.save()

        elif so_object.status == 2:
            # return from customer

            if returned == 1:
                so_object.status = 3 
                so_object.Returned_date = datetime.datetime.now()

                for cproduct in so_object.product_ids.all():
                    product = cproduct.product_id
                    product.quatity += cproduct.quantity
                    product.save()
                    product.make_stock_status()
                    product.save()

            else:
                # closed purchase-order
                so_object.status = 4
                so_object.closed_date = datetime.datetime.now()

        so_object.save()

        return redirect('/sales-order/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return'] = int(self.request.path.split('/')[-1])

        return context


# sales Order Delete
class SalesOrderDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = SalesOrder
    template_name = 'pages/modals/sales-order/so-delete.html'
    success_message = 'Success: Selected Sales Order was deleted.'
    success_url = reverse_lazy('sales-order')

# Sales Order Details for documents
def SalesOrderDetailsAdd(request, pk):
    customer = SalesOrder.objects.get(pk=pk)
    return HttpResponse(serializers.serialize("json", [customer]), content_type="application/json")

def DropDownOptions(request):
    invoices = Invoice.objects.filter(mode=SALES_ORDER_MODE)
    options = []

    for order in SalesOrder.objects.all():
        for invoice in invoices:
                if not order.id == invoice.related_so.id:
                    options.append('Sales Order (' + order.id + ')')


    return JsonResponse({ 'options' :  options})
