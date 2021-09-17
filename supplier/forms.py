from django import forms
from .models import Supplier

class SupplierRegister(forms.ModelForm):

    id = forms.CharField(
        label='Supplier Id',
        widget=forms.TextInput(
            attrs={               
                "class": "form-control"
            }
        ))

    company = forms.CharField(
        label='Enter Company Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Company Name",                
                "class": "form-control"
            }
        ))

    name = forms.CharField(
        label='Enter Supplier\'s First Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Customer\'s First Name",                
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        label='Enter Email Address',
        help_text='Required',
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email Address",                
                "class": "form-control"
            }
        ))

    mobile_number = forms.CharField(
        label='Enter Mobile Number',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Mobile No",                
                "class": "form-control"
            }
        ))

    fax_number = forms.CharField(
        label='Enter Fax Number',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Fax No",                
                "class": "form-control"
            }
        ))

    Address_1 = forms.CharField(
        label='Enter Postal Address 1',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Postal Address 1",                
                "class": "form-control"
            }
        ))

    Address_2 = forms.CharField(
        label='Enter Postal Address 2',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Postal Address 2",                
                "class": "form-control"
            }
        ))

    city = forms.CharField(
        label='Enter Postal City',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Postal City",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Supplier
        fields = ('id', 'company','name', 'email', 'mobile_number','fax_number', 
                'Address_1', 'Address_2', 'city')