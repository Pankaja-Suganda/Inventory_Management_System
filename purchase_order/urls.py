from django.urls import path
from .views import *

urlpatterns = [
    path('purchase-order/', PurchaseOrderList.as_view(), name='purchase-order'),
    path('purchase-order/<str:pk>', PurchaseOrderDetails.as_view(), name='purchase-order'),
    path('update-status/<str:pk>', update_status, name='update-status')

]