from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Customer
from app.views import context_packer
# Create your views here.

@login_required(login_url="/login/")
def customer_info(request, id):
    print('customer_info : ', id)
    context = {}
    context['0'] = context_packer(Customer, "c_customer", id)

    request.session['context'] = context
    return redirect('/customers.html')

@login_required(login_url="/login/")
def customer_delete(request, id):
    print('customer_delete : ', id)
    return redirect('/customers.html')

@login_required(login_url="/login/")
def customer_update(request, id):
    print('customer_update : ', id)
    return redirect('/customers.html')