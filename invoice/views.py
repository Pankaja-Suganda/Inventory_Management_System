from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from .models import Invoice, Invoice_Product
from .filters import InvoiceFilter
from .forms import InvoiceForm, InvoicProductFormSet

from customer.models import Customer
from authentication.models import BaseUser
from sales_order.models import SalesOrder
from stock.models import Product
from pre_sales_order.models import PreSalesOrder

from bootstrap_modal_forms.generic import BSModalDeleteView



# Create your views here.
# Invoice list
class InvoiceList(LoginRequiredMixin, generic.ListView):
    model = Invoice
    context_object_name = "Invoices"
    template_name = 'pages/billing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = InvoiceFilter(self.request.GET, queryset=Invoice.objects.all())
        context['Invoices'] = context['filter'].qs
        context['total'] = Invoice.objects.all().count()
        # context['issued'] = PreSalesOrder.objects.filter(status=0).count()
        # context['produced'] = PreSalesOrder.objects.filter(status=1).count()
        # context['delivered'] = PreSalesOrder.objects.filter(status=2).count()
        # context['returned'] = PreSalesOrder.objects.filter(status=3).count()
        # context['closed'] = PreSalesOrder.objects.filter(status=4).count()
        context['create'] = 1
        context['segment'] = 'billing'
        return context

# sales order Details
class InvoiceDetails(LoginRequiredMixin, generic.detail.DetailView):
    model = Invoice
    context_object_name = "Invoice_selected"
    template_name = 'pages/billing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = InvoiceFilter(self.request.GET, queryset=Invoice.objects.all())
        context['Invoices'] = context['filter'].qs
        context['total'] = Invoice.objects.all().count()
        # context['issued'] = PreSalesOrder.objects.filter(status=0).count()
        # context['produced'] = PreSalesOrder.objects.filter(status=1).count()
        # context['delivered'] = PreSalesOrder.objects.filter(status=2).count()
        # context['returned'] = PreSalesOrder.objects.filter(status=3).count()
        # context['closed'] = PreSalesOrder.objects.filter(status=4).count()
        context['segment'] = 'billing'
        context['create'] = 0
        return context

# create Invoice view
class InvoiceDocTemplate(LoginRequiredMixin, generic.CreateView):
    template_name = 'documents/invoice-doc.html'
    model=Invoice
    form_class = InvoiceForm
    success_url = reverse_lazy('billing')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = 0
        context['invoice_id'] = Invoice.invoice_id()
        context['date'] = datetime.datetime.now()
        context['form_set'] = InvoicProductFormSet() 

        return context

    def post(self, request, *args, **kwargs):
        invoice_form = InvoiceForm(request.POST or None)
        formset_form = InvoicProductFormSet(request.POST or None)

        # invoice form validation checking
        if invoice_form.is_valid():
            invoice = invoice_form.save()

        option = int(invoice_form.cleaned_data['option'])

        if option == 0:
            # generating invoice from sales order
            so = invoice.related_so
            for ref_product in so.product_ids.all():
                product = Invoice_Product(
                    invoice_id = invoice,
                    product_id = Product.objects.filter(name=ref_product.product_id).first(),
                    quantity = ref_product.quantity
                )
                product.save()
                invoice.product_ids.add(product)
                print(ref_product, product, invoice, product.product_id, ref_product.quantity, product.total_price)
            invoice.customer_id = so.customer_id
            invoice.save()

        elif option == 1:
            # generating invoice from Pre sales order
            pso = invoice.related_pso
            for ref_product in pso.product_ids.all():
                product = Invoice_Product(
                    invoice_id = invoice,
                    product_id = Product.objects.filter(name=ref_product.product_id).first(),
                    quantity = ref_product.quantity
                )
                product.save()
                invoice.product_ids.add(product)
                print(ref_product, product, invoice, product.product_id, ref_product.quantity, product.total_price)
            invoice.customer_id = pso.customer_id
            invoice.save()

        elif option == 2:
            # generating invoice from manual formset
            # if formset_form.is_valid():
            #     for form_product in formset_form:
            #         if form_product.is_valid():
            #             form_product.save()
            print("looping")

        return redirect('invoice-doc')

# creating invoicce
def create_invoice(request):
    context = {}
    context['create'] = 0

    return redirect('/billing/', context)

# preview the issued Invoice
class invoice_view(generic.TemplateView):
    template_name = 'documents/invoice-doc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            invoice_id = self.request.path.rsplit('/', 1)[-1]
            context['Invoice'] = Invoice.objects.filter(id=invoice_id).first()
            context['other_count'] = range(context['Invoice'].product_ids.count()+1, (10+context['Invoice'].product_ids.count()) - context['Invoice'].product_ids.count())
        context['segment'] = 'billing'
        context['user'] = self.request.user

        # create = 1 for preview window
        context['create'] = 1
        return context

# Invoice Delete
class InvoiceDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Invoice
    template_name = 'pages/modals/invoice/invoice-delete.html'
    success_message = 'Success: Selected Pre Sales Order was deleted.'
    success_url = reverse_lazy('billing')