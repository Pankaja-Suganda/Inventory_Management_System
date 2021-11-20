from django.contrib import admin
from .models import Color, Size, ProductCategories, Product, Product_Material
# Register your models here.

class MaterialInLineAdmin(admin.TabularInline):
    model = Product_Material

class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [MaterialInLineAdmin]

admin.site.register(Product, PurchaseOrderAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product_Material)
admin.site.register(ProductCategories)