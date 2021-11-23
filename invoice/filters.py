from django_filters import fields, FilterSet
import django_filters
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Invoice
from customer.models import Customer


class InvoiceFilter(FilterSet):
    id = django_filters.CharFilter(
        field_name='id',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={           
                "placeholder" : "By ID..",         
                "class": "form-control in"
            }
        )
        )
    
    issued_date = django_filters.DateRangeFilter(
            widget=forms.Select(
            attrs={           
                "placeholder" : "By ID..",         
                "class": "form-control in"
            }
        )
    )

    customer_id = django_filters.ModelChoiceFilter(
            queryset=Customer.objects.all(),
            widget=forms.Select(
            attrs={           
                "placeholder" : "By ID..",         
                "class": "form-control in"
            }
        ))

    class Meta:
        model = Invoice
        fields = ('id', 'issued_date', 'customer_id')