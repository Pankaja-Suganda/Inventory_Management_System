# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import BaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.password_validation import validate_password

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    user_name = forms.CharField(
        label='Enter Username',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
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

    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES,
        label='Select Gender',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Gender",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        label='Enter Password',
        help_text='Required',
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        label='Enter Password Again',
        help_text='Required',
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Repeat Password",                
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        label='Enter First Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        label='Enter Last Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",                
                "class": "form-control"
            }
        ))

    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female')
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES,
        label='Select Gender',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Gender",                
                "class": "form-control"
            }
        ))

    Address_1 = forms.CharField(
        label='Enter Address 1',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address 1",                
                "class": "form-control"
            }
        ))
    Address_2 = forms.CharField(
        label='Enter Address 2',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address 2",                
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
    city = forms.CharField(
        label='Enter City',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "City",                
                "class": "form-control"
            }
        ))

    JOB_ROLES = [
    ('manager','MANAGER'),
    ('executive','EXECUTIVE'),
    ('staff','STAFF')
    ]
    role = forms.ChoiceField(choices=JOB_ROLES,
        label='Select Designation',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Role",                
                "class": "form-control"
            }
        ))
    is_staff = forms.BooleanField(
        label='is Stafff ',
        help_text='Required',
        widget=forms.CheckboxInput(
            attrs={
                "placeholder" : "is Staff",                
                "class": "form-control"
            }
        ))
    is_active = forms.BooleanField(
        label='is activated',
        help_text='Required',
        widget=forms.CheckboxInput(
            attrs={
                "placeholder" : "Account Activate",                
                "class": "form-control"
            }
        ))

    profile_img = forms.ImageField(
        label='Select Profile Image',
        help_text='Required',
        error_messages = {'invalid': "Image files only"})

    class Meta:
        model = BaseUser
        fields = ('user_name', 'email', 'password1', 'gender', 'profile_img',
                  'password2', 'first_name', 'last_name', 'gender',
                  'mobile_number', 'Address_1', 'Address_2', 'city','role',
                  'is_staff', 'is_active')

class ProfileUpdate(forms.ModelForm):
    user_name = forms.CharField(
        label='Enter Username',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
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
    first_name = forms.CharField(
        label='Enter First Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        label='Enter Last Name',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",                
                "class": "form-control"
            }
        ))

    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES,
        label='Select Gender',
        help_text='Required',
        widget=forms.Select(
            attrs={
                "placeholder" : "Gender",                
                "class": "form-control"
            }
        ))

    Address_1 = forms.CharField(
        label='Enter Address 1',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address 1",                
                "class": "form-control"
            }
        ))
    Address_2 = forms.CharField(
        label='Enter Address 2',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address 2",                
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
    city = forms.CharField(
        label='Enter City',
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "City",                
                "class": "form-control"
            }
        ))

    profile_img = forms.ImageField(
        label='Select Profile Image',
        help_text='Required',
        error_messages = {'invalid': "Image files only"})

    class Meta:
        model = BaseUser
        fields = ('user_name', 'email', 'first_name', 'last_name', 'gender',
                  'mobile_number', 'Address_1', 'Address_2', 'city', 'profile_img')

class UserPasswordUpdate(forms.ModelForm):
    
    old_password  = forms.CharField(
        label='Enter Old Password',
        help_text='Required',
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Old Password",                
                "class": "form-control"
            }
        ))

    password1 = forms.CharField(
        label='Enter Password',
        help_text='Required',
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        label='Enter Password Again',
        help_text='Required',
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Repeat Password",                
                "class": "form-control"
            }
        ))

    def check_password(self, user):
        state = False
        if not user.check_password(self.cleaned_data['old_password']):
            self.add_error('old_password', 'User current Authentication is failed - check it out')
        else:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']

            try:
                validate_password(password1, user)
            except forms.ValidationError as error:
                self.add_error('password1', error)
                
            if not self.has_error('password1'):
                if password1 and password2:
                    if password1 != password2:
                        self.add_error('password2', 'Both password and password repeat must be the same - check it out')
                    else:
                        state = True
            
        return state

        

    class Meta:
        model = BaseUser
        fields = ['old_password', 'password1', 'password2']
