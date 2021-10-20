from django.contrib import admin
from .models import CMaterial, PurchaseOrder
# Register your models here.
admin.site.register(PurchaseOrder)
admin.site.register(CMaterial)