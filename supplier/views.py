from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Supplier
from app.views import context_packer
# Create your views here.

@login_required(login_url="/login/")
def supplier_info(request, id):
    context = {}
    context['0'] = context_packer(Supplier, "c_Supplier", id)

    request.session['context'] = context
    return redirect('/suppliers.html')