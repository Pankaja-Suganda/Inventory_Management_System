from django.urls import path
from .views import *

urlpatterns = [
    path('billing/', InvoiceList.as_view(), name='billing'),
    path('billing/<str:pk>', InvoiceDetails.as_view(), name='billing'),
    # path('update-status-quote/<str:pk>/<str:return>', QuatationStatusUpdateView.as_view(), name='update-status-quote'),
    path('create-invoice/', create_invoice, name='create-invoice'),
    path('preview-invoice/<str:pk>', invoice_view.as_view(), name='preview-invoice'),
    path('delete-invoice/<str:pk>', InvoiceDeleteView.as_view(), name="delete-invoice"),

    # documents
    path('invoice-doc/', InvoiceDocTemplate.as_view(), name="invoice-doc"),
    
]