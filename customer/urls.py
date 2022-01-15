from django.urls import path
from .views import *

urlpatterns = [
    path('customers/<str:pk>', CustomerDetails.as_view(), name='detail_customer'),
    path('detail_customer_add/<str:pk>', CustomerDetailsAdd, name="detail_customer_add"),
    path('customers/', CustomersList.as_view(), name='customers'),
    path('create_customer/', CustomerCreateView.as_view(), name='create_customer'),
    path('update_customer/<str:pk>', CustomerUpdateView.as_view(), name='update_customer'),
    path('delete_customer/<str:pk>', CustomerDeleteView.as_view(), name='delete_customer')
]