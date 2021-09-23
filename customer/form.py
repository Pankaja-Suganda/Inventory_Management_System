from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Customer

class CustomerRegister(BSModalModelForm):

    id = forms.CharField(
        label='Customer Id',
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

    first_name = forms.CharField(
        label='Enter Customer\'s First Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Customer\'s First Name",                
                "class": "form-control"
            }
        ))

    last_name = forms.CharField(
        label='Enter Customer\'s Last Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Customer\'s Last Name",                
                "class": "form-control"
            }
        ))

    STATUS_CHOICES = (
        (0, 'Active'),
        (1, 'Expired'),
        (2, 'Suspended')
    )
    
    status = forms.ChoiceField(choices=STATUS_CHOICES,
        label='Select Customer Status',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Customer Status",                
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        label='Enter Email Address',
        help_text='Required',
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
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

    Postal_Address_1 = forms.CharField(
        label='Enter Postal Address 1',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Postal Address 1",                
                "class": "form-control"
            }
        ))

    Postal_Address_2 = forms.CharField(
        label='Enter Postal Address 2',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Postal Address 2",                
                "class": "form-control"
            }
        ))

    Postal_city = forms.CharField(
        label='Enter Postal City',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Postal City",                
                "class": "form-control"
            }
        ))

    billing_Address_1 = forms.CharField(
        label='Enter Postal Address 1',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Postal Address 1",                
                "class": "form-control"
            }
        ))

    billing_Address_2 = forms.CharField(
        label='Enter Postal Address 2',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Postal Address 2",                
                "class": "form-control"
            }
        ))

    billing_city = forms.CharField(
        label='Enter Postal City',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Postal City",                
                "class": "form-control"
            }
        ))
    
    customer_img = forms.ImageField(
        label='Select Profile Image',
        help_text='Required',
        error_messages = {'invalid': "Image files only"})

    class Meta:
        model = Customer
        fields = ('id', 'company','first_name', 'last_name', 'status', 
                  'email', 'mobile_number', 'Postal_Address_1', 'Postal_Address_2', 
                  'Postal_city', 'billing_Address_1', 'billing_Address_2', 'billing_city', 'customer_img')


