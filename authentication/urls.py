# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', login_view, name="login"),
    path("logout/", logout_user, name="logout"),
    path('update/', UserUpdate.as_view(), name="update"),
    # path('reset_pass', ResetPassword, name="reset_pass"),
    # path('SetUserPermissions', SetUserPermissions, name="SetUserPermissions"),
    # path('deleteUser', deleteUser, name="deleteUser"),

    path('register/', UserRegistration.as_view(), name="register"),
    path('settings/', UserList.as_view(), name="settings_permissions"),
    path('update_user/<int:pk>', UserUpdateView.as_view(), name='update_user'),
    path('delete_user/<int:pk>', UserDeleteView.as_view(), name='delete_user')

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)