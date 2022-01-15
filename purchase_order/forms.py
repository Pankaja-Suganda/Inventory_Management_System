from django import forms
from django.forms.models import  inlineformset_factory
from materials.models import Materials
from supplier.models import Supplier
from .models import CMaterial, PurchaseOrder
from bootstrap_modal_forms.forms import BSModalModelForm

class CMaterialForm(forms.ModelForm):
    material_id = forms.ModelChoiceField(
        queryset = Materials.objects.all(),
        label='Select Material',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Material",                
                "class": "form-control"
            }
        ))

    quantity = forms.FloatField(
        label='Enter Quatity of Material',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "step": '0.01',
                "placeholder" : "Quantity",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = CMaterial
        fields = ('material_id', 'quantity')

CMaterialFormSet = inlineformset_factory(
                        PurchaseOrder,
                        CMaterial,
                        form=CMaterialForm,
                        can_delete=True,
                        extra=9
                    )

class PurchaseOrderForm(forms.ModelForm):
    id = forms.CharField(
        label='PO Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    supplier_id = forms.ModelChoiceField(
        queryset = Supplier.objects.all(),
        label='Select Supplier',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Supplier",                
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
    # tax rate is removed
    # tax_rate = forms.FloatField(
    #     label='Enter the Tax Rate',
    #     widget=forms.NumberInput(
    #         attrs={
    #             "placeholder" : " ",                
    #             "class": "form-control"
    #         }
    #     ))

    description = forms.CharField(
        label='Enter Description of Category',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description of creating category", 
                'rows':3,               
                "class": "form-control"
            }
        ))

    class Meta:
        model = PurchaseOrder
        fields = ('id', 'supplier_id', 'discount_persentage', 'description')

class PurchaseOrderStatusForm(BSModalModelForm):
    id = forms.CharField(
        label='PO Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",

            }
        ))

    class Meta:
        model = PurchaseOrder
        fields = ('id',)