# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    username = forms.CharField(
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


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 
                  'password2', 'first_name', 'last_name')
