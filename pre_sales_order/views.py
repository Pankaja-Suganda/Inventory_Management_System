from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.views.generic.base import TemplateView
from .models import PreSalesOrder, PProduct
from .filters import PreSalesOrderFilter
from .forms import PreSalesOrderForm, PProductForm, PProductlFormSet, PreSalesOrderStatusForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from django.http import HttpResponse
from django.core import serializers

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

# Create your views here.
# sales order list
class PreSalesOrderList(LoginRequiredMixin, generic.ListView):
    model = PreSalesOrder
    context_object_name = "PreSalesOrders"
    template_name = 'pages/pre-sales-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PreSalesOrderFilter(self.request.GET, queryset=PreSalesOrder.objects.all())
        context['PreSalesOrders'] = context['filter'].qs
        context['total'] = PreSalesOrder.objects.all().count()
        context['issued'] = PreSalesOrder.objects.filter(status=0).count()
        context['produced'] = PreSalesOrder.objects.filter(status=1).count()
        context['delivered'] = PreSalesOrder.objects.filter(status=2).count()
        context['returned'] = PreSalesOrder.objects.filter(status=3).count()
        context['closed'] = PreSalesOrder.objects.filter(status=4).count()
        context['create'] = 1
        context['segment'] = 'pre-sale-order'
        return context

# sales order Details
class PreSalesOrderDetails(LoginRequiredMixin, generic.detail.DetailView):
    model = PreSalesOrder
    context_object_name = "PSO_selected"
    template_name = 'pages/pre-sales-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PreSalesOrderFilter(self.request.GET, queryset=PreSalesOrder.objects.all())
        context['PreSalesOrders'] = context['filter'].qs
        context['total'] = PreSalesOrder.objects.all().count()
        context['issued'] = PreSalesOrder.objects.filter(status=0).count()
        context['produced'] = PreSalesOrder.objects.filter(status=1).count()
        context['delivered'] = PreSalesOrder.objects.filter(status=2).count()
        context['returned'] = PreSalesOrder.objects.filter(status=3).count()
        context['closed'] = PreSalesOrder.objects.filter(status=4).count()
        context['segment'] = 'pre-sale-order'
        context['create'] = 0
        return context

# create so view
class PreSalesOrderDocTemplate(LoginRequiredMixin, generic.CreateView):
    template_name = 'documents/pre-sales-order-doc.html'
    model=PreSalesOrder
    form_class = PreSalesOrderForm
    context_object_name = "PSO_form"
    success_url = reverse_lazy('pre-sales-order-doc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = 0
        context['pso_id'] = PreSalesOrder.pso_id()
        context['date'] = datetime.datetime.now()
        context['form_set'] = PProductlFormSet() 

        return context

    def form_valid(self, form):

        if self.request.method == 'POST':
            ctx = self.get_context_data()
            form_set = PProductlFormSet(self.request.POST or None)
            pso_id = PreSalesOrderForm(self.request.POST)

            # checking whether the product quantity is enough or not
            checked_status = False
            if form_set.is_valid():
                for form_product in form_set:
                    if form_product.is_valid() and not len(form_product.cleaned_data) == 0 :
                        product = form_product.cleaned_data['product_id']
                        quantity = form_product.cleaned_data['quantity']

                        for Cmaterial in product.material_ids.all():
                            required_quantity = Cmaterial.quantity * quantity
                            if required_quantity >  float(Cmaterial.material_id.quatity):
                                checked_status = True
                                raise forms.ValidationError('Available Material ' + Cmaterial.material_id.name + ' quantity is ' + str(Cmaterial.material_id.quatity) +', Required quantity is ' + str(required_quantity) + ', thus, Product Quatity is not enough for Pre sales order')
            
            if not checked_status:
                if pso_id.is_valid():
                    pso_id = pso_id.s ave()
                
                for form_product in form_set:
                    product = form_product.save(commit=False)
                    if form_product.is_valid() and not product.product_id==None and not product.quantity==0:
                        product.pso_id = pso_id
                        product.save()
                        pso_id.product_ids.add(product)

                return super(PreSalesOrderDocTemplate, self).form_valid(form)
                
# creating so
def create_pso(request):
    context = {}
    context['create'] = 0

    return redirect('/pre-sales-order/', context)

# preview the generated PSO
class pso_view(generic.TemplateView):
    template_name = 'documents/pre-sales-order-doc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            po_id = self.request.path.rsplit('/', 1)[-1]
            context['Order'] = PreSalesOrder.objects.filter(id=po_id)[0]
            context['other_count'] = range(context['Order'].product_ids.count()+1, (10+context['Order'].product_ids.count()) - context['Order'].product_ids.count())
        context['segment'] = 'pre-sale-order'
        context['user'] = self.request.user

        # create = 1 for preview window
        context['create'] = 1
        return context

# Sales Order Update
class PreStatusUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = PreSalesOrder
    template_name = 'pages/modals/sales-order/so-info.html'
    form_class  = PreSalesOrderStatusForm
    success_message = 'Success: Selected Pre Sales Order\' status was updated.'
    success_url = reverse_lazy('pre-sales-order')

    def post(self, request, *args, **kwargs):

        so_object = PreSalesOrder.objects.filter(id=request.POST.get('id')).first()
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
            # Closing the PSO 
            so_object.status = 4
            so_object.closed_date = datetime.datetime.now()


            # for cproduct in so_object.product_ids.all():
            #     product = cproduct.product_id
            #     product.quatity -= cproduct.quantity
            #     product.save()
            #     product.make_stock_status()
            #     product.save()

        # no retrrn and sending
        # elif so_object.status == 2:
        #     # return from customer

        #     if returned == 1:
        #         so_object.status = 3 
        #         so_object.Returned_date = datetime.datetime.now()

        #         for cproduct in so_object.product_ids.all():
        #             product = cproduct.product_id
        #             product.quatity += cproduct.quantity
        #             product.save()
        #             product.make_stock_status()
        #             product.save()

        #     else:
        #         # closed purchase-order
        #         so_object.status = 4
        #         so_object.closed_date = datetime.datetime.now()
                
        so_object.save()

        return redirect('/pre-sales-order/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return'] = int(self.request.path.split('/')[-1])

        return context


# sales Order Delete
class PreSalesOrderDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = PreSalesOrder
    template_name = 'pages/modals/sales-order/so-delete.html'
    success_message = 'Success: Selected Pre Sales Order was deleted.'
    success_url = reverse_lazy('pre-sales-order')


# Pre Sales Order Details for documents
def PreSalesOrderDetailsAdd(request, pk):
    customer = PreSalesOrder.objects.get(pk=pk)
    return HttpResponse(serializers.serialize("json", [customer]), content_type="application/json")

