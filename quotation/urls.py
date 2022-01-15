from django.urls import path
from .views import *

urlpatterns = [
    path('quatation/', QuotationList.as_view(), name='quatation'),
    path('quatation/<str:pk>', QuotationDetails.as_view(), name='quatation'),
    path('update-status-quote/<str:pk>/<str:return>', QuatationStatusUpdateView.as_view(), name='update-status-quote'),
    path('create-quote/', create_quote, name='create-quote'),
    path('preview-quote/<str:pk>', quote_view.as_view(), name='preview-quote'),
    path('delete-quotation/<str:pk>', QuotationDeleteView.as_view(), name="delete-quotation"),

    # documents
    path('quotation-doc/', QuotationDocTemplate.as_view(), name="quotation-doc"),
    
]