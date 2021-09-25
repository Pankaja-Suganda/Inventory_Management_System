from django.urls import path
from .views import *

urlpatterns = [
    path('customers/<str:pk>', CustomerDetails.as_view(), name='detail_customer'),
    path('customers/', CustomersList.as_view(), name='customers'),
    path('create/', CustomerCreateView.as_view(), name='create_customer'),
    path('update/<str:pk>', CustomerUpdateView.as_view(), name='update_customer'),
    path('delete/<str:pk>', CustomerDeleteView.as_view(), name='delete_customer')
]