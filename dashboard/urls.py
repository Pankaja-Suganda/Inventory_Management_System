from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', MorrisDemo.as_view()),
    path('invoice_dataset/<int:index>/<str:value>', invoice_dataset, name='invoice_dataset'),
    path('stock_dataset/<int:index>/<str:value>', stock_dataset, name='stock_dataset'),
    path('material_dataset/<int:index>', material_dataset, name='material_dataset'),
    path('purchase_dataset/<int:index>/<str:value>', purchase_dataset, name='purchase_dataset'),
    path('sales_dataset/<int:index>/<str:value>', sales_dataset, name='sales_dataset'),
    path('overview_dataset/<int:index>', sales_dataset, name='overview_dataset'),

]