from django.urls import path
from .views import *

urlpatterns = [
    path('suppliers/<str:pk>', SupplierDetails.as_view(), name="detail_supplier"),
    path('detail_supplier_add/<str:pk>', SupplierDetailsAdd, name="detail_supplier_add"),
    path('suppliers/', SuppliersList.as_view(), name="suppliers"),
    path('create_supplier/', SupplierCreateView.as_view(), name="create_supplier"),
    path('update_supplier/<str:pk>', SupplierUpdateView.as_view(), name="update_supplier"),
    path('delete_supplier/<str:pk>', SupplierDeleteView.as_view(), name="delete_supplier"),

]