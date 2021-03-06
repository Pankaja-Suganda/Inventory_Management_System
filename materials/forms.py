from django import forms
from .models import Shell, Categories, Materials, Color, Size
from supplier.models import Supplier
from authentication.models import BaseUser
import shortuuid
from bootstrap_modal_forms.forms import BSModalModelForm

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

class CategoryCreate(BSModalModelForm):

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
                "placeholder" : "Description of creating category",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Categories
        fields = ('id', 'name', 'description')
    
class CategoryUpdate(BSModalModelForm):

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
        label='Enter Category Description',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description of Updating category",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Categories
        fields = ('id', 'name', 'description')
    
class ShellCreate(BSModalModelForm):
    id = forms.CharField(
        label='Shell Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    status = forms.ChoiceField(choices=Shell.STATUS_CHOICES,
        label='Shell Status',
        initial=0,
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Shell Status",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        label='Enter Shell Description',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description of Shell contains",                
                "class": "form-control"
            }
        ))

    row = forms.IntegerField(
        label='Enter Row Number',
        help_text='Required',
        initial='0',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Row Number",                
                "class": "form-control"
            }
        ))

    column = forms.IntegerField(
        label='Enter Column Number',
        help_text='Required',
        initial='0',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Column Number",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Shell
        fields = ('id', 'row', 'column', 'description', 'status')

class ShellUpdate(BSModalModelForm):

    id = forms.CharField(
        label='Shell Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    status = forms.ChoiceField(choices=Shell.STATUS_CHOICES,
        label='Shell Status',
        initial=0,
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Shell Status",                
                "class": "form-control",
            }
        ))

    description = forms.CharField(
        label='Enter Shell Description',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description of Shell contains",                
                "class": "form-control"
            }
        ))

    row = forms.IntegerField(
        label='Enter Row Number',
        help_text='Required',
        initial='0',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Row Number",                
                "class": "form-control"
            }
        ))

    column = forms.IntegerField(
        label='Enter Column Number',
        help_text='Required',
        initial='0',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Column Number",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Shell
        fields = ('id', 'row', 'column', 'description', 'status')

class MaterialsCreate(BSModalModelForm):
    id = forms.CharField(
        label='Material Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control",
                "readonly": True
            }
        ))

    name = forms.CharField(
        label='Enter Material Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Material Name",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        label='Enter Material Description',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Material Description",                
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

    stock_margin = forms.IntegerField(
        label='Enter Stock Margin of Material',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Stock Margin",                
                "class": "form-control"
            }
        ))

    category_id = forms.ModelChoiceField(
        queryset = Categories.objects.all(),
        label='Select Category',
        widget=forms.Select(
            attrs={
                "placeholder" : "Category",                
                "class": "form-control"
            }
        ))

    shell_id = forms.ModelChoiceField(
        queryset = Shell.objects.all(),
        label='Select Shell',
        required=False, 
        widget=forms.Select(
            attrs={
                "placeholder" : "Shell",                
                "class": "form-control"
            }
        ))

    supplier_id = forms.ModelChoiceField(
        queryset = Supplier.objects.all(),
        label='Select Supplier',
        widget=forms.Select(
            attrs={
                "placeholder" : "Supplier",                
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
        model = Materials
        fields = ('id', 'name', 'description', 'unit_price', 'stock_margin', 'category_id', 'shell_id', 'supplier_id', 'color_id', 'Size_id')

class MaterialsUpdate(BSModalModelForm):

    name = forms.CharField(
        label='Enter Material Name',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Material Name",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        label='Enter Material Description',
        help_text='Required',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Material Description",                
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

    stock_margin = forms.IntegerField(
        label='Enter Stock Margin of Material',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Stock Margin",                
                "class": "form-control"
            }
        ))

    category_id = forms.ModelChoiceField(
        queryset = Categories.objects.all(),
        label='Select Category',
        widget=forms.Select(
            attrs={
                "placeholder" : "Category",                
                "class": "form-control"
            }
        ))

    shell_id = forms.ModelChoiceField(
        queryset = Shell.objects.all(),
        label='Select Shell',
        required=False, 
        widget=forms.Select(
            attrs={
                "placeholder" : "Shell",                
                "class": "form-control"
            }
        ))

    supplier_id = forms.ModelChoiceField(
        queryset = Supplier.objects.all(),
        label='Select Supplier',
        required=False, 
        widget=forms.Select(
            attrs={
                "placeholder" : "Supplier",                
                "class": "form-control"
            }
        ))

    color_id = forms.ModelChoiceField(
        queryset = Color.objects.all(),
        label='Select Color',
        required=False, 
        widget=forms.Select(
            attrs={
                "placeholder" : "Product Color",                
                "class": "form-control"
            }
        ))

    Size_id = forms.ModelChoiceField(
        queryset = Size.objects.all(),
        label='Select Size',
        required=False, 
        widget=forms.Select(
            attrs={
                "placeholder" : "Product Size",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Materials
        fields = ('name', 'description', 'unit_price', 'category_id', 'shell_id',
         'supplier_id', 'stock_margin', 'color_id', 'Size_id')