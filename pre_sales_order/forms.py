from django import forms
from django.forms.models import  inlineformset_factory
from stock.models import Product
from customer.models import Customer
from .models import PProduct, PreSalesOrder
from bootstrap_modal_forms.forms import BSModalModelForm

class PProductForm(forms.ModelForm):
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
        model = PProduct
        fields = ('product_id', 'quantity')

PProductlFormSet = inlineformset_factory(
                        PreSalesOrder,
                        PProduct,
                        form=PProductForm,
                        can_delete=True,
                        extra=9
                    )

class PreSalesOrderForm(forms.ModelForm):
    id = forms.CharField(
        label='Pre Sales Order Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    customer_id = forms.ModelChoiceField(
        queryset = Customer.objects.all(),
        label='Select Customer',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Customer",                
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
        label='Enter Description of Sales Order',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description of Sales Order", 
                'rows':3,               
                "class": "form-control"
            }
        ))

    class Meta:
        model = PreSalesOrder
        fields = ('id', 'customer_id', 'discount_persentage', 'description')

class PreSalesOrderStatusForm(BSModalModelForm):
    id = forms.CharField(
        label='PSO Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",

            }
        ))

    class Meta:
        model = PreSalesOrder
        fields = ('id',)