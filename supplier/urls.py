from django.urls import path
from .views import supplier_info

urlpatterns = [
    path('supplier_info/<str:id>', supplier_info, name="supplier_info")
]