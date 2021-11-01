from django.urls import path
from .views import *

urlpatterns = [
    path('purchase-order/', PurchaseOrderList.as_view(), name='purchase-order'),
    path('purchase-order/<str:pk>', PurchaseOrderDetails.as_view(), name='purchase-order'),
    path('update-status/<str:pk>', update_status, name='update-status'),
    path('create-po/', create_po, name='create-po'),
    path('preview-po/<str:pk>', po_view.as_view(), name='preview-po'),

    # documents
    path('purchase-order-doc/', PurchaseOrderDocTemplate.as_view(), name="purchase-order-doc"),
]