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

from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (
  BSModalUpdateView,
  BSModalDeleteView
)

from .forms import LoginForm, SignUpForm, ProfileUpdate, UserPasswordUpdate, UserUpdatePer
from .models import BaseUser

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
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True

        else:
            msg = 'Form is not valid'    
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
    context['select'] = 'account-update'
    context['form_reset'] = UserPasswordUpdate(instance=request.user)
    context['update_success'] = False

    if request.method == "POST":
        profile_img = request.FILES.get('profile_img') 
        form = ProfileUpdate(request.POST, 
                            request.FILES,
                            instance=request.user)
        form.profile_img = profile_img
        print (form.is_valid(), form.errors)
        if form.is_valid():
            form.save() 
            context['update_success'] = True
            context['form'] = ProfileUpdate(instance=request.user)
            return redirect('settings.html', context)
        else:
            context['form'] = form
            # context['user'] = request.user

    return render(request, 'settings.html', context)


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
        'form': ProfileUpdate(instance=request.user),
        'select':'account-change-password' 
    })

@login_required(login_url="/login/")
def SetUserPermissions(request):
    context = {}
    pk = request.POST.get("id")
    _is_active = bool(request.POST.get("is_active"))
    _is_staff = bool(request.POST.get("is_staff"))

    context['select'] = 'account-permissions'
    if request.method == 'POST':
        user = BaseUser.objects.filter(id=pk).update(
        is_staff = _is_staff,
        is_active = _is_active)

    context['form_per'] = UserUpdatePer()
    context['select'] = 'account-permissions' 
    
    return redirect('settings.html', context)

@login_required(login_url="/login/")
def deleteUser(request):    
    pk = request.POST.get("id")
    print ('delete id ', pk)
    try:
        user = BaseUser.objects.get(id = pk)
        user.delete()
        messages.success(request, "The user is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User does not exist")    
        return render(request, 'settings.html')

    except Exception as e: 
        return render(request, 'settings.html',{'error':e.message})

    return redirect('settings.html')

# user information update
class UserUpdate(generic.UpdateView):
    model = BaseUser
    context_object_name = "customers"
    form_class = ProfileUpdate
    template_name = 'settins/update.html'
    success_url = reverse_lazy('settings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print ('updating : ', context)
        return context


# User registraion
class UserRegistration(generic.CreateView):
    model = BaseUser
    form_class = SignUpForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            form = SignUpForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                form.save()
                messages.success(self.request, ' User in Successfully Added to the System!')
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=raw_password)
            else:
                messages.error(self.request, 'You Entered Data To the Form is Invail, Please Try Again!')
        return context


# user list wth pagination
class UserList(generic.ListView):
    model = BaseUser
    paginate_by = 7
    context_object_name = "users"
    template_name = 'pages/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileUpdate(instance=self.request.user)
        context['form_reset'] = UserPasswordUpdate()
        context['segment'] = 'settings'
        context['num_of_objects'] = BaseUser.objects.count()
        tab = self.request.GET.get('tab')
        context['select'] = 'account-general'
        if not tab == None:
            if int(tab) == 0:context['select'] = 'account-general'
            if int(tab) == 1:context['select'] = 'account-update'
            if int(tab) == 2:context['select'] = 'account-change-password'
            if int(tab) == 3:context['select'] = 'account-permissions'
        else:
            context['select'] = 'account-permissions'
        return context

# user permission Update
class UserUpdateView(BSModalUpdateView):
    model = BaseUser
    template_name = 'pages/modals/user-permission-update.html'
    form_class = UserUpdatePer
    success_message = 'Success: Selected User was updated.'
    success_url = reverse_lazy('settings_permissions')
    # failure_url = reverse_lazy('settings')

# user Delete
class UserDeleteView(BSModalDeleteView):
    model = BaseUser
    template_name = 'pages/modals/user-delete.html'
    success_message = 'Success: Selected user was deleted.'
    success_url = reverse_lazy('settings_permissions')
    # failure_url = reverse_lazy('settings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = 'account-permissions'
        return context