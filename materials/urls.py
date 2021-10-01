from django.urls import path
from .views import *

urlpatterns = [
    path('materials/<str:pk>', MaterialsDetails.as_view(), name='detail_material'),
    path('materials/', MaterialsList.as_view(), name='materials'),
    path('create_material/', MaterialCreateView.as_view(), name='create_material'),
    path('update_material/<str:pk>', MaterialUpdateView.as_view(), name='update_material'),
    path('delete_material/<str:pk>', MaterialDeleteView.as_view(), name='delete_material'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('update_category/<str:pk>', CategoryUpdateView.as_view(), name='update_category'),
    path('delete_category/<str:pk>', CategoryDeleteView.as_view(), name='delete_category')
]