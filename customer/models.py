from django.db import models
import shortuuid

# Create your models here.
class Customer(models.Model):
    
    STATUS_CHOICES = (
        (0, 'Active'),
        (1, 'Expired'),
        (2, 'Suspended')
    )

    id = models.CharField(max_length=7, primary_key=True, blank=False)
    company = models.CharField('company', max_length=150, blank=True)
    first_name = models.CharField('first name', max_length=150, blank=True)
    last_name = models.CharField('last name', max_length=150,  blank=True)
    customer_img = models.ImageField(null=True, blank=False, upload_to='core/static/assets/images/customer', default='core/static/assets/images/customer/default.png')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    email = models.EmailField('email address', blank=True)
    mobile_number = models.IntegerField(max_length=10, blank=True)

    Postal_Address_1 = models.CharField('postal address 1', max_length=250, blank=False)
    Postal_Address_2 = models.CharField('postal address 2', max_length=250, blank=False)
    Postal_city = models.CharField('postal city', max_length=250, blank=False)

    billing_Address_1 = models.CharField('billing address 1', max_length=250, blank=False)
    billing_Address_2 = models.CharField('billing address 2', max_length=250, blank=False)
    billing_city = models.CharField('billing city', max_length=250, blank=False)
        
    joined_date = models.DateTimeField(auto_now=True)
    orders_count = models.IntegerField(blank=False, default=0)
    # last_order = 
    last_order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name
    
    def class_name(self):
        return self.__name__

    @staticmethod
    def customer_id():
        id_no = shortuuid.ShortUUID(alphabet="0123456789")
        full_id = 'C'+ str( id_no.random(length=6))
        check_id = Customer.objects.filter(id=full_id)

        while(check_id.exists()):
            id = shortuuid.ShortUUID(alphabet="0123456789")
            full_id = 'C'+ str( id_no.random(length=6))
            check_id = Customer.objects.filter(id=full_id)

        return full_id
    
    class Meta:
        __name__ = 'Customer'

    # def save(self)