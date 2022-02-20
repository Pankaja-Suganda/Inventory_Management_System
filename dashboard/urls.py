from django.urls import path
from .views import *

urlpatterns = [
    path('', DashBoardTemplate.as_view()),
    path('invoice_dataset/<int:index>/<str:value>', invoice_dataset, name='invoice_dataset'),
    path('stock_material_dataset/', stock_material_dataset, name='stock_material_dataset'),
    path('purchase_dataset/<int:index>/<str:value>', purchase_dataset, name='purchase_dataset'),
    path('sales_dataset/<int:index>/<str:value>', sales_dataset, name='sales_dataset'),
]