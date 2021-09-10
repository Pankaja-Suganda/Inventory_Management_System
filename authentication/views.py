# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, ProfileUpdate, UserPasswordUpdate

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

@login_required(login_url="/login/")
def register_user(request):

    msg     = None
    success = False
    context = {}

    if request.method == "POST":
        print ('register : ',request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    context['segment'] = 'register'
    context['form'] = form
    context['msg'] = msg
    context['success'] = success
    return render(request, "accounts/register.html", context )

@login_required(login_url="/login/")
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/login/")
def UpdateAccount(request):
    context = {}

    if request.method == "POST":
        profile_img = request.FILES.get('profile_img') 
        form = ProfileUpdate(request.POST, 
                            request.FILES,
                            instance=request.user)
        form.profile_img = profile_img

        if form.is_valid():
            form.save() 
            context['form'] = form
        else:
            context['form'] = form

    return redirect('settings.html', context)

@login_required(login_url="/login/")
def ResetPassword(request):
    success = False

    if request.method == 'POST':
        form = UserPasswordUpdate(instance=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            user.check_password(form.cleaned_data['password1'])
            state = form.check_password(user)
            
            if state:
                user.set_password(form.cleaned_data['password1'])
                user.save()
                update_session_auth_hash(request, request.user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                success = True
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserPasswordUpdate(instance=request.user)

    return render(request, 'settings.html', {
        'form_reset': form,
        'success' : success,
        'form': ProfileUpdate(instance=request.user)
    })