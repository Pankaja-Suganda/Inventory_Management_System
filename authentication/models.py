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

GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female')
)


class CustomAccountManager(BaseUserManager):
    def create_user(self, user_name, password):
        

        if not password:
            raise ValueError("You Must Provide Pasword")

        user = self.model(user_name = user_name)

        # if Group.objects.filter(name = user.role).exists():
        #     group = Group.objects.filter(name = user.role)
        #     user.groups.add(group)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = False 
        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_superuser(self, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser Must Be Assigned to is_staff = True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser Must Be Assigned to is_superuser = True')

        return self.create_user( user_name, password)

class BaseUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('email address', blank=True)
    user_name = models.CharField('user name', max_length=150, unique=True)
    first_name = models.CharField('first name', max_length=150, blank=True)
    last_name = models.CharField('last name', max_length=150, default='male')
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    profile_img = models.ImageField(null=True, blank=True, upload_to='core/static/assets/images/user', default='core/static/assets/images/user/default.png')
    mobile_number = models.IntegerField( blank=True)
    Address_1 = models.CharField('address 1', max_length=250, blank=True)
    Address_2 = models.CharField('address 2', max_length=250, blank=True)
    city = models.CharField('city', max_length=250, blank=True)
    role = models.CharField(max_length=10, choices=JOB_ROLES, default='staff')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

    class meta:
        proxy = True
        
    def __str__(self):
        return self.user_name

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name
    
