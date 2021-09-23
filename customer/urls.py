from django.urls import path
from .views import customer_info, customer_update, customer_delete

urlpatterns = [
    path('customer_info/<str:id>', customer_info, name="customer_info"),
    path('customer_delete/<str:id>', customer_delete, name="customer_delete"),
    path('customer_update/<str:id>', customer_update, name="customer_update")
]