import django_filters
from django_filters import fields, FilterSet
from django import forms

from .models import Supplier

class SupplierFilter(FilterSet):
    id = django_filters.CharFilter(
        field_name='id',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={           
                "placeholder" : "By ID..",         
                "class": "form-control in"
            }
        ))
    
    company = django_filters.CharFilter(
        field_name='company',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "By Company..",                
                "class": "form-control in "
            }
        ))

    po_count = django_filters.NumberFilter(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "By PO Count..",                
                "class": "form-control in "
            }
        ))

    class Meta:
        model = Supplier
        fields = ('id', 'company', 'po_count')