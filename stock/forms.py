from django import forms
from .models import Color, Size, Product, ProductCategories
from customer.models import Customer
from authentication.models import BaseUser
import shortuuid
from bootstrap_modal_forms.forms import BSModalModelForm

class CategoryForm(BSModalModelForm):

    id = forms.CharField(
        label='Category Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    name = forms.CharField(
        label='Enter Category Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Category Name",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        label='Enter Description of Category',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description of Category",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = ProductCategories
        fields = ('id', 'name', 'description')

class SizeForm(BSModalModelForm):

    id = forms.CharField(
        label='Size Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    name = forms.CharField(
        label='Enter the Size',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name of the Size ",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        label='Enter the Description of Size',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description of size",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Size
        fields = ('id', 'name', 'description')

class ColorForm(BSModalModelForm):

    id = forms.CharField(
        label='Color Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    name = forms.CharField(
        label='Enter the Color Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name of the Color ",                
                "class": "form-control"
            }
        ))

    color = forms.CharField(
        label='Select the Color Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name of the Color ",                
                "class": "form-control",
                "type" : "color",
                "height" : "50px"

            }
        ))


    description = forms.CharField(
        label='Enter the Description of Color',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description of Color",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Color
        fields = ('id', 'name', 'color', 'description')

class ProductForm(BSModalModelForm):
    id = forms.CharField(
        label='Product Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    name = forms.CharField(
        label='Enter the Product Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Product Name",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        label='Enter the Product Description',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Product Description",                
                "class": "form-control"
            }
        ))

    unit_price = forms.FloatField(
        label='Enter Unit Price of Product',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Unit Price",                
                "class": "form-control"
            }
        ))

    stock_margin = forms.IntegerField(
        label='Enter Stock Margin of Product',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Stock Margin",                
                "class": "form-control"
            }
        ))

    category_id = forms.ModelChoiceField(
        queryset = ProductCategories.objects.all(),
        label='Select Category',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Category",                
                "class": "form-control"
            }
        ))

    color_id = forms.ModelChoiceField(
        queryset = Color.objects.all(),
        label='Select Color',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Product Color",                
                "class": "form-control"
            }
        ))

    Size_id = forms.ModelChoiceField(
        queryset = Size.objects.all(),
        label='Select Size',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Product Size",                
                "class": "form-control"
            }
        ))


    class Meta:
        model = Product
        fields = ('id','name', 'description', 'unit_price', 'category_id', 'color_id',
         'Size_id', 'stock_margin')

class ProductUpdateForm(BSModalModelForm):

    name = forms.CharField(
        label='Enter the Product Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Product Name",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        label='Enter the Product Description',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Product Description",                
                "class": "form-control"
            }
        ))

    unit_price = forms.FloatField(
        label='Enter Unit Price of Product',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Unit Price",                
                "class": "form-control"
            }
        ))

    stock_margin = forms.IntegerField(
        label='Enter Stock Margin of Product',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Stock Margin",                
                "class": "form-control"
            }
        ))

    category_id = forms.ModelChoiceField(
        queryset = ProductCategories.objects.all(),
        label='Select Category',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Category",                
                "class": "form-control"
            }
        ))

    color_id = forms.ModelChoiceField(
        queryset = Color.objects.all(),
        label='Select Color',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Product Color",                
                "class": "form-control"
            }
        ))

    Size_id = forms.ModelChoiceField(
        queryset = Size.objects.all(),
        label='Select Size',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Product Size",                
                "class": "form-control"
            }
        ))


    class Meta:
        model = Product
        fields = ('name', 'description', 'unit_price', 'category_id', 'color_id',
         'Size_id', 'stock_margin')