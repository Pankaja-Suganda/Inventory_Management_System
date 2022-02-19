# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.
class Company(models.Model):
    """
    The basic Company details are handing by this class for automatic 
    document generation

    """
    
    id = models.AutoField(primary_key=True, blank=False)
    company = models.CharField('company', max_length=150, blank=True)
    first_name = models.CharField('first name', max_length=150, blank=True)
    last_name = models.CharField('last name', max_length=150,  blank=True)
    email = models.EmailField('email address', blank=True)
    mobile_number = models.IntegerField( blank=True)

    Postal_Address_1 = models.CharField('postal address 1', max_length=250, blank=False)
    Postal_Address_2 = models.CharField('postal address 2', max_length=250, blank=False)
    Postal_city = models.CharField('postal city', max_length=250, blank=False)

    billing_Address_1 = models.CharField('billing address 1', max_length=250, blank=False)
    billing_Address_2 = models.CharField('billing address 2', max_length=250, blank=False)
    billing_city = models.CharField('billing city', max_length=250, blank=False)

    def __str__(self):
        """
        The object string retriving function

        Returns:
            string: The name of the Company 
        """
        return self.company

    def get_last_name(self):
        """
        The owner's Last name retriving function

        Returns:
            string: The last name of company owner
        """
        return self.last_name

    def get_first_name(self):
        """
        The owner's first name retriving function

        Returns:
            string: The first name of company owner
        """

        return self.first_name
    
    def class_name(self):
        """
        The class name retriving function

        Returns:
            string: The name of the class
        """
        return self.__name__
    
    class Meta:
        """
        The Meta data of 'Company' Class
        """
        __name__ = 'Company'

