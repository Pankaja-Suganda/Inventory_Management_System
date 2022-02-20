# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path('docs/', include('django_mkdocs.urls', namespace='docmentation')), # Django
    url('tech-docs/', include('docs.urls')),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("customer.urls")),        # customer url
    path("", include("supplier.urls")),        # supplier url
    path("", include("materials.urls")),       # materials url
    path("", include("purchase_order.urls")),  # purchase_order url
    path("", include("sales_order.urls")),     # sales_order url
    path("", include("pre_sales_order.urls")),     # pre_sales_order url
    path("", include("quotation.urls")),     # quotation url
    path("", include("invoice.urls")),     # invoice url
    path("", include("dashboard.urls")),     # Dashboard url
    path("", include("stock.urls")),             # stock urls
    
    path("", include("app.urls")),          # UI Kits Html files 
    
]
