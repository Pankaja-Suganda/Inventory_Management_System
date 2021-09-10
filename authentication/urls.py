# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, logout_user, UpdateAccount, ResetPassword
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register.html', register_user, name="register"),
    path("logout/", logout_user, name="logout"),
    path('update', UpdateAccount, name="update"),
    path('reset_pass', ResetPassword, name="reset_pass")
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)