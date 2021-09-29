from django import forms
from .models import Shell, Categories, Materials
from supplier.models import Supplier
import shortuuid
from bootstrap_modal_forms.forms import BSModalModelForm

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
        label='Enter Category Description',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Category Description",                
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
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Category Description",                
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

    row = forms.IntegerField(
        label='Enter Row Number',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Row Number",                
                "class": "form-control"
            }
        ))

    column = forms.IntegerField(
        label='Enter Column Number',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Column Number",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Shell
        fields = ('id', 'row', 'column')

class ShellUpdate(BSModalModelForm):

    row = forms.IntegerField(
        label='Enter Row Number',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Row Number",                
                "class": "form-control"
            }
        ))

    column = forms.IntegerField(
        label='Enter Column Number',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Column Number",                
                "class": "form-control"
            }
        ))

    shell_state = forms.ChoiceField(choices=Shell.STATUS_CHOICES,
        label='Select Customer Status',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Customer Status",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Shell
        fields = ('row', 'column', 'shell_state')

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
        widget=forms.TextInput(
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

    category_id = forms.ModelChoiceField(
        choices = Categories.objects.all(),
        label='Select Category',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Category",                
                "class": "form-control"
            }
        ))

    shell_id = forms.ModelChoiceField(
        choices = Shell.objects.all(),
        label='Select Shell',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Shell",                
                "class": "form-control"
            }
        ))

    supplier_id = forms.ModelChoiceField(
        choices = Supplier.objects.all(),
        label='Select Supplier',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Supplier",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Materials
        fields = ('id', 'name', 'description', 'unit_price', 'category_id', 'shell_id', 'supplier_id')

class MaterialsUpdate(BSModalModelForm):

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
        widget=forms.TextInput(
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

    quatity = forms.IntegerField(
        label='Enter Quatity of Material',
        help_text='Required',
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Quatity of Materials",                
                "class": "form-control"
            }
        ))

    status = forms.ChoiceField(
        choices=Materials.STATUS_CHOICES,
        label='Select Material Status',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Material Status",                
                "class": "form-control"
            }
        ))

    category_id = forms.ModelChoiceField(
        choices = Categories.objects.all(),
        label='Select Category',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Category",                
                "class": "form-control"
            }
        ))

    shell_id = forms.ModelChoiceField(
        choices = Shell.objects.all(),
        label='Select Shell',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Shell",                
                "class": "form-control"
            }
        ))

    supplier_id = forms.ModelChoiceField(
        choices = Supplier.objects.all(),
        label='Select Supplier',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Supplier",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Materials
        fields = ('name', 'description', 'unit_price', 'category_id', 'shell_id',
         'supplier_id', 'quatity', 'status')