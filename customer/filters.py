from django_filters import fields, FilterSet
import django_filters
from django import forms
from .models import Customer

class CustomerFilter(FilterSet):
    id = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={           
                "placeholder" : "By ID..",         
                "class": "form-control in"
            }
        ))

    company = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "By Company..",                
                "class": "form-control in "
            }
        ))

    STATUS_CHOICES = (
        (0, 'Active'),
        (1, 'Expired'),
        (2, 'Suspended')
    )
    
    status = django_filters.ChoiceFilter(choices=STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder" : "By Status",                
                "class": "form-control in"
            }
        ))

    class Meta:
        model = Customer
        fields = ('id', 'company', 'status')