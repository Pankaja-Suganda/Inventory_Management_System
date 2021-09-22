from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Customer
from app.views import context_packer
# Create your views here.

@login_required(login_url="/login/")
def customer_info(request, id):
    context = {}
    context['0'] = context_packer(Customer, "c_customer", id)

    request.session['context'] = context
    return redirect('/customers.html')