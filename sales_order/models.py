from django.db import models
from django.db.models import Sum
import datetime
import shortuuid
from customer.models import Customer
from stock.models import Product
from authentication.models import BaseUser


# SO Model
class SalesOrder(models.Model):
    STATUS_CHOICES = (
        (0, 'Issued'),
        (1, 'Producing'),
        (2, 'Sended'),
        (3, 'Returned'),
        (4, 'Closed')
    )

    id = models.CharField(max_length=11, primary_key=True, blank=False)
    user_id = models.ForeignKey(BaseUser, blank=True, null=True, on_delete=models.SET_NULL)
    customer_id = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    product_ids = models.ManyToManyField('CProduct', blank=True, null=True)
    total_price = models.FloatField(blank=False, default=0.0)
    sub_total_price = models.FloatField(blank=False, default=0.0)
    discount_persentage = models.FloatField(blank=False, default=0.0)
    tax_rate = models.FloatField(blank=False, default=0.0)
    issued_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    Produced_date = models.DateTimeField(blank=True, null=True)
    Sended_date = models.DateTimeField(blank=True, null=True)
    Returned_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    so_pdf = models.FileField(null=True, blank=True, upload_to='core/static/assets/documents/purchase order/')
    description = models.TextField(blank=True)

    def get_id(self):
        return self.id

    def class_name(self):
        return self.__class__.__name__
    
    # def save(self, *args, **kwargs):
        
    #     if self.status == 0:
    #         # calculations
    #         for material in self.material_ids.all():
    #             self.sub_total_price += material.total_price
    #         self.total_price = self.sub_total_price - (self.sub_total_price*(self.discount_persentage/100))

    #         # supplier po count increment
    #         self.supplier_id.po_count += 1
    #         # assigning supplier last po date
    #         self.supplier_id.last_order_date = self.issued_date
    #         self.supplier_id.save()

    #     super(SalesOrder, self).save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     # decrease the po_count of the supplier 
    #     self.supplier_id.po_count -= 1
    #     self.supplier_id.save()

    #     if self.status == 2:
    #         for cmaterial in self.material_ids.all():
    #             material = cmaterial.material_id
    #             material.quatity -= cmaterial.quantity
    #             material.save()
    #             material.make_stock_status()
    #             material.save()
    #     super(SalesOrder, self).delete(*args, **kwargs)
    
    @staticmethod
    def so_id():
        id_no = shortuuid.ShortUUID(alphabet="0123456789")
        full_id = 'SO-'+ str( id_no.random(length=8))
        check_id = SalesOrder.objects.filter(id=full_id)

        while(check_id.exists()):
            id_no = shortuuid.ShortUUID(alphabet="0123456789")
            full_id = 'SO-'+ str( id_no.random(length=8))
            check_id = SalesOrder.objects.filter(id=full_id)

        return full_id

# SO Supportive model
class CProduct(models.Model):
    id = models.AutoField(primary_key=True)
    so_id = models.ForeignKey(SalesOrder, blank=True, null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(blank=False, null=False, default=0)
    total_price = models.FloatField(blank=False, default=0.0)
    
    def save(self, *args, **kwargs):
        self.total_price = abs(self.quantity) * abs(self.product_id.unit_price)
        super(CProduct, self).save(*args, **kwargs)