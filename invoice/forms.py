from django import forms
from django.forms.models import  inlineformset_factory
from stock.models import Product
from sales_order.models import SalesOrder
from pre_sales_order.models import PreSalesOrder
from customer.models import Customer
from .models import Invoice_Product, Invoice
from bootstrap_modal_forms.forms import BSModalModelForm


SALES_ORDER_MODE = 1
PRE_SALES_ORDER_MODE = 2

class Invoice_ProductForm(forms.ModelForm):
    product_id = forms.ModelChoiceField(
        queryset = Product.objects.all(),
        label='Select the Product',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Product",                
                "class": "form-control"
            }
        ))

    unit_price = forms.FloatField(
        label='Enter Unit Price of Material',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Unit Price",                
                "class": "form-control"
            }
        ))

    quantity = forms.IntegerField(
        label='Enter Quatity of the Product',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Quantity",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Invoice_Product
        fields = ('product_id', 'quantity', 'unit_price')

InvoicProductFormSet = inlineformset_factory(
                        Invoice,
                        Invoice_Product,
                        form=Invoice_ProductForm,
                        can_delete=True,
                        extra=9
                    )

def modeFilter(mode, objects):

    objects_copy = objects
    if mode == SALES_ORDER_MODE:
        invoices = Invoice.objects.filter(mode=SALES_ORDER_MODE)
    elif mode == PRE_SALES_ORDER_MODE:
        invoices = Invoice.objects.filter(mode=PRE_SALES_ORDER_MODE)

    for order in objects:
        for invoice in invoices:
            if invoice.related_so:
                if order.id == invoice.related_so.id:
                    objects_copy = objects_copy.exclude(id=order.id)

    # print('objects : ', objects)
    # print('filtered objects : ', objects_copy)

    return objects_copy

class InvoiceForm(forms.ModelForm):
    id = forms.CharField(
        label='Invoice Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    customer_id = forms.ModelChoiceField( 
        queryset = Customer.objects.all(),
        label='Select Customer',
        required=False,
        widget=forms.Select(
            attrs={
                "placeholder" : "Customer",                
                "class": "form-control"
            }
        ))

    related_so = forms.ModelChoiceField(
        queryset = modeFilter(SALES_ORDER_MODE, SalesOrder.objects.all()),
        label='Select Sales Order',
        required=False,
        widget=forms.Select(
            attrs={
                "placeholder" : "Sales Order",                
                "class": "form-control"
            }
        ))

    related_pso = forms.ModelChoiceField(
        queryset = modeFilter(PRE_SALES_ORDER_MODE, PreSalesOrder.objects.all()),
        label='Select Pre Sales Order',
        required=False,
        widget=forms.Select(
            attrs={
                "placeholder" : "Pre Sales Order",                
                "class": "form-control"
            }
        ))

    discount_persentage = forms.FloatField(
        label='Enter the Discount',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : " ",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        label='Enter Description of Quotation',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description of Invoice", 
                'rows':3,               
                "class": "form-control"
            }
        ))

    OPTION_CHOICES = (
        (0, 'From Sales Order'),
        # (1, 'From Pre Sales Order'),
        (2, 'From Manual')
    )

    option = forms.ChoiceField(
        choices = OPTION_CHOICES,
        label='Select Invoice Option',
        widget=forms.Select(
            attrs={
                "placeholder" : "Options",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Invoice
        fields = ('id', 'customer_id', 'discount_persentage', 'related_so', 'related_pso' ,'description', 'option')
