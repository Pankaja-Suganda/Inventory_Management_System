from django.contrib import admin
from .models import Color, Size, ProductCategories, Product
# Register your models here.
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductCategories)
admin.site.register(Product)