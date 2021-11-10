from os import name
from django.db import models
from colorfield.fields import ColorField
from authentication.models import BaseUser
from customer.models import Customer
import shortuuid

# size Model
class Size(models.Model):
    id = models.CharField(max_length=7, primary_key=True, blank=False)
    name = models.CharField( max_length=150, blank=False)
    description = models.CharField( max_length=350, blank=False)

    def class_name(self):
        return self.__name__

    @staticmethod
    def size_id():
        id_no = shortuuid.ShortUUID(alphabet="0123456789")
        full_id = 'S'+ str( id_no.random(length=4))
        check_id = Size.objects.filter(id=full_id)

        while(check_id.exists()):
            id = shortuuid.ShortUUID(alphabet="0123456789")
            full_id = 'S'+ str( id.random(length=2))
            check_id = Size.objects.filter(id=full_id)

        return full_id
    
    class Meta:
        __name__ = 'Size'

# color Model
class Color(models.Model):
    id = models.CharField(max_length=7, primary_key=True, blank=False)
    name = models.CharField( max_length=150, blank=False)
    color = ColorField(format='hexa', default='#FF0000')
    description = models.CharField( max_length=350, blank=False)

    def class_name(self):
        return self.__name__

    @staticmethod
    def color_id():
        id_no = shortuuid.ShortUUID(alphabet="0123456789")
        full_id = 'C'+ str( id_no.random(length=2))
        check_id = Color.objects.filter(id=full_id)

        while(check_id.exists()):
            id = shortuuid.ShortUUID(alphabet="0123456789")
            full_id = 'C'+ str( id.random(length=2))
            check_id = Color.objects.filter(id=full_id)

        return full_id
    
    class Meta:
        __name__ = 'Color'


# Category Model
class ProductCategories(models.Model):
    id = models.CharField(max_length=7, primary_key=True, blank=False)
    name = models.CharField( max_length=150, blank=False)
    description = models.CharField( max_length=350, blank=False)

    def class_name(self):
        return self.__name__

    @staticmethod
    def category_id():
        id_no = shortuuid.ShortUUID(alphabet="0123456789")
        full_id = 'PCAT'+ str( id_no.random(length=4))
        check_id = ProductCategories.objects.filter(id=full_id)

        while(check_id.exists()):
            id = shortuuid.ShortUUID(alphabet="0123456789")
            full_id = 'PCAT'+ str( id.random(length=4))
            check_id = ProductCategories.objects.filter(id=full_id)

        return full_id
    
    class Meta:
        __name__ = 'Product_Categories'


# product Model
class Product(models.Model):

    STATUS_CHOICES = (
        (0, 'In Stock'),
        (1, 'Out Stock'),
    )

    id = models.CharField(max_length=12, primary_key=True, blank=False)
    name = models.CharField( max_length=150, blank=False)
    description = models.CharField( max_length=500, blank=False)
    unit_price =models.FloatField(blank=False)
    quatity = models.PositiveIntegerField( blank=False, default=0)
    stock_margin = models.PositiveIntegerField( blank=False, default=0)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=0)
    category_id = models.ForeignKey(ProductCategories, blank=True, null=True, on_delete=models.SET_NULL)
    color_id = models.ForeignKey(Color, blank=True, null=True, on_delete=models.SET_NULL)
    Size_id = models.ForeignKey(Size, blank=True, null=True, on_delete=models.SET_NULL)
    # shell_id = models.ForeignKey(Shell, blank=True, null=True, on_delete=models.SET_NULL)
    customers_id = models.ManyToManyField(Customer, blank=True, null=True)
    user_id = models.ForeignKey(BaseUser, blank=True, null=True, on_delete=models.SET_NULL)
    added_date = models.DateTimeField(auto_now=True)

    def make_stock_status(self):
        if self.quatity > self.stock_margin:
            self.status = 0
        else:
            self.status = 1

    @staticmethod
    def prodcut_id():
        id_no = shortuuid.ShortUUID(alphabet="0123456789")
        full_id = 'P'+ str( id_no.random(length=6))
        check_id = Product.objects.filter(id=full_id)

        while(check_id.exists()):
            id = shortuuid.ShortUUID(alphabet="0123456789")
            full_id = 'P'+ str( id.random(length=6))
            check_id = Product.objects.filter(id=full_id)

        return full_id

    def class_name(self):
        return self.__name__

    class Meta:
        __name__ = 'Product'
