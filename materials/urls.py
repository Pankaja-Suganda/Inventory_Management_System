from django.urls import path
from .views import *

urlpatterns = [
    path('materials/<str:pk>', MaterialsDetails.as_view(), name='detail_material'),
    path('materials/', MaterialsList.as_view(), name='materials'),
    path('create_material/', MaterialCreateView.as_view(), name='create_material'),
    path('update_material/<str:pk>', MaterialUpdateView.as_view(), name='update_material'),
    path('delete_material/<str:pk>', MaterialDeleteView.as_view(), name='delete_material'),

    # path('categories/<str:pk>', MaterialsDetails.as_view(), name='detail_category'),
    path('categories/<str:pk>/', CategoriesDetails.as_view(), name='categorys'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('update_category/<str:pk>', CategoryUpdateView.as_view(), name='update_category'),
    path('delete_category/<str:pk>', CategoryDeleteView.as_view(), name='delete_category'),

    path('shells/', ShellsList.as_view(), name='shells'),
    path('create_shell/', ShellCreateView.as_view(), name='create_shell'),
    path('update_shell/<str:pk>', ShellUpdateView.as_view(), name='update_shell'),
    path('delete_shell/<str:pk>', ShellDeleteView.as_view(), name='delete_shell'),
    
    # Size functions
    path('material_create_size/', SizeCreateView.as_view(), name='material_create_size'),
    path('material_update_size/<str:pk>', SizeUpdateView.as_view(), name='material_update_size'),
    path('material_delete_size/<str:pk>', SizeDeleteView.as_view(), name='material_delete_size'),

    # color functions
    path('material_create_color/', ColorCreateView.as_view(), name='material_create_color'),
    path('material_update_color/<str:pk>', ColorUpdateView.as_view(), name='material_update_color'),
    path('material_delete_color/<str:pk>', ColorDeleteView.as_view(), name='material_delete_color'),

]