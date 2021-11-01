# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('customers/', CustomerTemplate.as_view(), name="customers"),
    path('suppliers/', SupplierTemplate.as_view(), name="suppliers"),
    path('settings/', SettingsTemplate.as_view(), name="settings"),
    path('register/', RegisterTemplate.as_view(), name="register"),
    path('materials/', MaterialsTemplate.as_view(), name="materials"),
    path('shells/', ShellsTemplate.as_view(), name="shells"),
    path('purchase-order/', PurchaseOrderTemplate.as_view(), name="purchase-order"),
    path('items/', ItemsTemplate.as_view(), name="items"),
    path('sales-order/', SalesOrderTemplate.as_view(), name="sales-order"),
    path('pre-sales-order/', PreSalesOrderTemplate.as_view(), name="pre-sales-order"),
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
