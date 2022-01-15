from django.contrib import admin

# Register your models here.
from .models import Invoice, Invoice_Product

class InvoiceProductInLineAdmin(admin.TabularInline):
    model = Invoice_Product

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceProductInLineAdmin]

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Invoice_Product)