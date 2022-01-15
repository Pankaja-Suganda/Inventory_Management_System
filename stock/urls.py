from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ProdcutsList.as_view(), name="items"),

    # category functions
    path('create_product_category/', ProductCategoryCreateView.as_view(), name='create_product_category'),
    path('update_product_category/<str:pk>', ProductCategoryUpdateView.as_view(), name='update_product_category'),
    path('delete_product_category/<str:pk>', ProductCategoryDeleteView.as_view(), name='delete_product_category'),

    # Size functions
    path('create_size/', SizeCreateView.as_view(), name='create_size'),
    path('update_size/<str:pk>', SizeUpdateView.as_view(), name='update_size'),
    path('delete_size/<str:pk>', SizeDeleteView.as_view(), name='delete_size'),

    # color functions
    path('create_color/', ColorCreateView.as_view(), name='create_color'),
    path('update_color/<str:pk>', ColorUpdateView.as_view(), name='update_color'),
    path('delete_color/<str:pk>', ColorDeleteView.as_view(), name='delete_color'),

    # product functions
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<str:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<str:pk>', ProductDeleteView.as_view(), name='delete_product'),
]
