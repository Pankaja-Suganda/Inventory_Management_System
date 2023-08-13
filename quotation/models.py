from django.db import models
from django.db.models import Sum
import datetime
import shortuuid
from customer.models import Customer
from stock.models import Product
from authentication.models import BaseUser


# Quotation Model
class Quotation(models.Model):
    STATUS_CHOICES = (
        (0, 'Issued'),
        (1, 'Accepted'),
        (2, 'Rejected')
    )

    id = models.CharField(max_length=8, primary_key=True, blank=False)
    user_id = models.ForeignKey(BaseUser, blank=True, null=True, on_delete=models.SET_NULL)
    customer_id = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    product_ids = models.ManyToManyField('QProduct', blank=True)
    total_price = models.FloatField(blank=False, default=0.0)
    sub_total_price = models.FloatField(blank=False, default=0.0)
    discount_persentage = models.FloatField(blank=False, default=0.0)
    issued_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    accepted_date = models.DateTimeField(blank=True, null=True)
    rejected_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    quote_pdf = models.FileField(null=True, blank=True, upload_to='core/static/assets/documents/quotations/')
    description = models.TextField(blank=True)

    def get_id(self):
        return self.id

    def save(self, *args, **kwargs):
        
        if self.status == 0:
            self.sub_total_price = 0
            self.total_price = 0
            # calculations
            for product in self.product_ids.all():
                self.sub_total_price += product.total_price
            self.total_price = self.sub_total_price - (self.sub_total_price*(self.discount_persentage/100))

        super(Quotation, self).save(*args, **kwargs)

    def class_name(self):
        return self.__class__.__name__
    
    @staticmethod
    def quate_id():
        id_no = shortuuid.ShortUUID(alphabet="0123456789")
        full_id = 'Q-'+ str( id_no.random(length=6))
        check_id = Quotation.objects.filter(id=full_id)

        while(check_id.exists()):
            id_no = shortuuid.ShortUUID(alphabet="0123456789")
            full_id = 'Q-'+ str( id_no.random(length=6))
            check_id = Quotation.objects.filter(id=full_id)

        return full_id

# Quotation Supportive model
class QProduct(models.Model):
    id = models.AutoField(primary_key=True)
    quote_id = models.ForeignKey(Quotation, blank=True, null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(blank=False, null=False, default=0)
    unit_price = models.FloatField(blank=False, default=0.0)
    total_price = models.FloatField(blank=False, default=0.0)
    
    def save(self, *args, **kwargs):
        self.total_price = abs(self.quantity) * abs(self.unit_price)
        super(QProduct, self).save(*args, **kwargs)

