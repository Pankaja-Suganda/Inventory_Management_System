from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .models import Quotation, QProduct
from .filters import QuotationFilter
from .forms import QuotationForm, QProductForm, QProductlFormSet, QuotationStatusForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

# Create your views here.
# Quotation list
class QuotationList(LoginRequiredMixin, generic.ListView):
    model = Quotation
    context_object_name = "Quotations"
    template_name = 'pages/quatation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = QuotationFilter(self.request.GET, queryset=Quotation.objects.all())
        context['Quotations'] = context['filter'].qs
        context['total'] = Quotation.objects.all().count()
        context['issued'] = Quotation.objects.filter(status=0).count()
        context['accepted'] = Quotation.objects.filter(status=1).count()
        context['rejected'] = Quotation.objects.filter(status=2).count()
        context['create'] = 1
        context['segment'] = 'quatation'
        return context

# Quotation Details
class QuotationDetails(LoginRequiredMixin, generic.detail.DetailView):
    model = Quotation
    context_object_name = "Q_selected"
    template_name = 'pages/quatation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = QuotationFilter(self.request.GET, queryset=Quotation.objects.all())
        context['Quotations'] = context['filter'].qs
        context['total'] = Quotation.objects.all().count()
        context['issued'] = Quotation.objects.filter(status=0).count()
        context['accepted'] = Quotation.objects.filter(status=1).count()
        context['rejected'] = Quotation.objects.filter(status=2).count()
        context['segment'] = 'quatation'
        context['create'] = 0
        return context

# create Quotation view
class QuotationDocTemplate(LoginRequiredMixin, generic.CreateView):
    template_name = 'documents/quatation-doc.html'
    model=Quotation
    form_class = QuotationForm
    context_object_name = "form"
    success_url = reverse_lazy('quotation-doc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = 0
        context['quote_id'] = Quotation.quate_id()
        context['date'] = datetime.datetime.now()
        context['form_set'] = QProductlFormSet() 

        return context

    def form_valid(self, form):

        if self.request.method == 'POST':
            ctx = self.get_context_data()
            form_set = QProductlFormSet(self.request.POST or None)
            quate_id = QuotationForm(self.request.POST)
            if quate_id.is_valid():
                quate_id = quate_id.save()

            if form_set.is_valid():
                for form_product in form_set:
                    product = form_product.save(commit=False)
                    if form_product.is_valid() and not product.product_id==None and not product.quantity==0:
                        product.quote_id = quate_id
                        product.save()
                        quate_id.product_ids.add(product)

        return super(QuotationDocTemplate, self).form_valid(form)

# creating quotation
def create_quote(request):
    context = {}
    context['create'] = 0

    return redirect('/quatation/', context)

# preview the generated quatation
class quote_view(generic.TemplateView):
    template_name = 'documents/quatation-doc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            po_id = self.request.path.rsplit('/', 1)[-1]
            context['Quote'] = Quotation.objects.filter(id=po_id)[0]
            context['other_count'] = range(context['Quote'].product_ids.count()+1, (10+context['Quote'].product_ids.count()) - context['Quote'].product_ids.count())
        context['segment'] = 'quatation'
        context['user'] = self.request.user

        # create = 1 for preview window
        context['create'] = 1
        return context

# Sales Order Update
class QuatationStatusUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Quotation
    template_name = 'pages/modals/quotation/quote-info.html'
    form_class  = QuotationStatusForm
    success_message = 'Success: Selected Quotation\' status was updated.'
    success_url = reverse_lazy('sales-order')

    def post(self, request, *args, **kwargs):

        quote = Quotation.objects.filter(id=request.POST.get('id')).first()
        returned = int(request.path.split('/')[-1])

        if quote.status == 0:
            # accepted quotations 
            if returned == 0:
                quote.status = 1 
                quote.accepted_date = datetime.datetime.now()
            else:
                quote.status = 2
                quote.rejected_date = datetime.datetime.now()
                
        quote.save()

        return redirect('/quatation/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return'] = int(self.request.path.split('/')[-1])

        return context


# Quotation Delete
class QuotationDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Quotation
    template_name = 'pages/modals/quotation/quote-delete.html'
    success_message = 'Success: Selected Quotation was deleted.'
    success_url = reverse_lazy('quatation')

