# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('customers/', CustomerTemplate.as_view(), name="customers"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
