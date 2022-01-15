from django.contrib import admin
from .models import Quotation, QProduct

class ProductInLineAdmin(admin.TabularInline):
    model = QProduct

class QuotationAdmin(admin.ModelAdmin):
    inlines = [ProductInLineAdmin]

admin.site.register(Quotation, QuotationAdmin)
admin.site.register(QProduct)