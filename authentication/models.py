# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.utils import timezone

# Create your models here.
# job role arrays
JOB_ROLES = [
    ('manager','MANAGER'),
    ('executive','EXECUTIVE'),
    ('staff','STAFF')
]

class BaseUser(AbstractBaseUser, PermissionsMixin):

    user_name = models.CharField('user name', max_length=150, unique=True)
    mobile_number = models.CharField(max_length=10, blank=True)
    Address_1 = models.CharField('address 1', max_length=250, blank=True)
    Address_2 = models.CharField('address 2', max_length=250, blank=True)
    city = models.CharField('city', max_length=250, blank=True)
    role = models.CharField(max_length=10, choices=JOB_ROLES, default='staff')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    class meta:
        proxy = True
    def __str__(self):
        return self.user_name

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name
    
