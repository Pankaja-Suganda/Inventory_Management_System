from django.urls import path
from .views import *

urlpatterns = [
    path('pre-sales-order/', PreSalesOrderList.as_view(), name='pre-sales-order'),
    path('pre-sales-order/<str:pk>', PreSalesOrderDetails.as_view(), name='pre-sales-order'),
    path('update-status-pre-sales/<str:pk>/<str:return>', PreStatusUpdateView.as_view(), name='update-status-pre-sales'),
    path('create-pso/', create_pso, name='create-pso'),
    path('preview-pso/<str:pk>', pso_view.as_view(), name='preview-pso'),
    path('delete-pre-sales-order/<str:pk>', PreSalesOrderDeleteView.as_view(), name="delete-pre-sales-order"),

    # documents
    path('pre-sales-order-doc/', PreSalesOrderDocTemplate.as_view(), name="pre-sales-order-doc"),
    
]