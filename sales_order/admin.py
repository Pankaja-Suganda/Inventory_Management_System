from django.contrib import admin
from .models import CProduct, SalesOrder
# Register your models here.
class ProductInLineAdmin(admin.TabularInline):
    model = CProduct

class SalesOrderAdmin(admin.ModelAdmin):
    inlines = [ProductInLineAdmin]

admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(CProduct)
