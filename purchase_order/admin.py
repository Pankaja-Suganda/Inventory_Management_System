from django.contrib import admin
from .models import CMaterial, PurchaseOrder
# Register your models here.
class MaterialInLineAdmin(admin.TabularInline):
    model = CMaterial

class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [MaterialInLineAdmin]

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(CMaterial)