# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BaseUser

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

    class Meta:
        model = BaseUser
        fields = ('user_name', 'email', 'password1', 
                  'password2', 'first_name', 'last_name',
                  'mobile_number', 'Address_1', 'Address_2', 'city','role',
                  'is_staff', 'is_active')
