from django_filters import fields, FilterSet
import django_filters
from django import forms

from .models import SalesOrder

class SalesOrderFilter(FilterSet):
    id = django_filters.CharFilter(
        field_name='id',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={           
                "placeholder" : "By ID..",         
                "class": "form-control in"
            }
        ))
        
    status = django_filters.ChoiceFilter(choices=SalesOrder.STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder" : "By Status",                
                "class": "form-control in"
            }
        ))

    class Meta:
        model = SalesOrder
        fields = ('id', 'status')