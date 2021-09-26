from django.db import models
import shortuuid

# Create your models here.
class Supplier(models.Model):


    id = models.CharField(max_length=7, primary_key=True, blank=False)
    company = models.CharField('company', max_length=150, blank=True)
    name = models.CharField('name', max_length=150, blank=True)
    supplier_img = models.ImageField(null=True, blank=False, upload_to='core/static/assets/images/supplier', default='core/static/assets/images/supplier/default.png')

    email = models.EmailField('email address', blank=True)
    mobile_number = models.IntegerField(max_length=10, blank=True)
    fax_number = models.IntegerField(max_length=10, blank=True)

    Address_1 = models.CharField('postal address 1', max_length=250, blank=False)
    Address_2 = models.CharField('postal address 2', max_length=250, blank=False)
    city = models.CharField('postal city', max_length=250, blank=False)
        
    joined_date = models.DateTimeField(auto_now=True)
    po_count = models.IntegerField(blank=False, default=0)
    # suppliering products from product model
    # last_order = 
    last_order_date = models.DateTimeField(auto_now=True)

    def get_id(self):
        return self.id

    def class_name(self):
        return self.__class__.__name__

    def get_company(self):
        return self.last_name
    
    @staticmethod
    def supplier_id():
        id = shortuuid.ShortUUID(alphabet="0123456789")
        return 'S'+ str( id.random(length=6))
