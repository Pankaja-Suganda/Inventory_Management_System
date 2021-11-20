from django.contrib import admin
from .models import PreSalesOrder, PProduct

class ProductInLineAdmin(admin.TabularInline):
    model = PProduct

class PreSalesOrderAdmin(admin.ModelAdmin):
    inlines = [ProductInLineAdmin]

admin.site.register(PreSalesOrder, PreSalesOrderAdmin)
admin.site.register(PProduct)