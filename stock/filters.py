from django_filters import fields, FilterSet
import django_filters
from django import forms

from .models import Product, ProductCategories, Color, Size

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
        model = ProductCategories
        fields = ('id', 'name')

class SizeFilter(FilterSet):
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
        model = Size
        fields = ('id', 'name')

class ColorFilter(FilterSet):
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
        model = Color
        fields = ('id', 'name')

# Product filter
class ProductFilter(FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr = 'icontains',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "By Name..",                
                "class": "form-control in "
            }
        ))

    status = django_filters.ChoiceFilter(choices=Product.STATUS_CHOICES,
        field_name='status',
        widget=forms.Select(
            attrs={
                "placeholder" : "By status",                
                "class": "form-control in"
            }
        ))

    class Meta:
        model = Product
        fields = ('name', 'status')