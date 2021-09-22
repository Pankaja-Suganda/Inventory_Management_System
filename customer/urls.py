from django.urls import path
from .views import customer_info

urlpatterns = [
    path('customer_info/<str:id>', customer_info, name="customer_info")
]