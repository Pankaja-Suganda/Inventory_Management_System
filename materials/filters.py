from django_filters import fields, FilterSet
import django_filters
from django import forms

from .models import Shell, Categories, Materials
from supplier.models import Supplier

class CategoryFilter(FilterSet):
    id = django_filters.CharFilter(
        field_name='id',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={           
                "placeholder" : "By ID..",         
                "class": "form-control in"
            }
        ))

    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "By Name..",                
                "class": "form-control in "
            }
        ))

    class Meta:
        model = Categories
        fields = ('id', 'name')

class ShellFilter(FilterSet):
    id = django_filters.CharFilter(
        field_name='id',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={           
                "placeholder" : "By ID..",         
                "class": "form-control in"
            }
        ))

    shell_state = django_filters.ChoiceFilter(choices=Shell.STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder" : "By State",                
                "class": "form-control in"
            }
        ))

    class Meta:
        model = Categories
        fields = ('id', 'shell_state')

class MaterialFilter(FilterSet):
    id = django_filters.CharFilter(
        field_name='id',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={           
                "placeholder" : "By ID..",         
                "class": "form-control in"
            }
        ))

    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "By Name..",                
                "class": "form-control in "
            }
        ))

    state = django_filters.ChoiceFilter(choices=Materials.STATUS_CHOICES,
        field_name='status',
        widget=forms.Select(
            attrs={
                "placeholder" : "By State",                
                "class": "form-control in"
            }
        ))

    category_id = django_filters.ChoiceFilter(choices=Categories.objects.all(),
        field_name='category_id',
        widget=forms.Select(
            attrs={
                "placeholder" : "By Category",                
                "class": "form-control in"
            }
        ))

    shell_id = django_filters.ChoiceFilter(choices=Shell.objects.all(),
        field_name='shell_id',
        widget=forms.Select(
            attrs={
                "placeholder" : "By Shell",                
                "class": "form-control in"
            }
        ))

    supplier_id = django_filters.ChoiceFilter(choices=Supplier.objects.all(),
        field_name='supplier_id',
        widget=forms.Select(
            attrs={
                "placeholder" : "By Supplier",                
                "class": "form-control in"
            }
        ))

    class Meta:
        model = Materials
        fields = ('id', 'name', 'state', 'category_id', 'shell_id', 'supplier_id')