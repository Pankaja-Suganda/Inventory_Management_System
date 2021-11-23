from django.db import models
from django.db.models import Sum
import datetime
import shortuuid
from customer.models import Customer
from sales_order.models import SalesOrder
from pre_sales_order.models import PreSalesOrder
from stock.models import Product
from authentication.models import BaseUser


# Quotation Model
class Invoice(models.Model):

    id = models.CharField(max_length=9, primary_key=True, blank=False)
    user_id = models.ForeignKey(BaseUser, blank=True, null=True, on_delete=models.SET_NULL)
    customer_id = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    product_ids = models.ManyToManyField('Invoice_Product', blank=True, null=True)
    total_price = models.FloatField(blank=False, default=0.0)
    sub_total_price = models.FloatField(blank=False, default=0.0)
    discount_persentage = models.FloatField(blank=False, default=0.0)
    issued_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.BooleanField(default=1)
    po_no = models.CharField(max_length=12, blank=True)
    related_so = models.ForeignKey(SalesOrder, blank=True, null=True, on_delete=models.SET_NULL)
    related_pso = models.ForeignKey(PreSalesOrder, blank=True, null=True, on_delete=models.SET_NULL)
    invoice_pdf = models.FileField(null=True, blank=True, upload_to='core/static/assets/documents/invoice/')
    description = models.TextField(blank=True)

    def get_id(self):
        return self.id

    def save(self, *args, **kwargs):
        # calculations
        print('calculations')
        for product in self.product_ids.all():
            self.sub_total_price += product.total_price
        self.total_price = self.sub_total_price - (self.sub_total_price*(self.discount_persentage/100))

        super(Invoice, self).save(*args, **kwargs)

    def class_name(self):
        return self.__class__.__name__
    
    @staticmethod
    def invoice_id():
        id_no = shortuuid.ShortUUID(alphabet="0123456789")
        full_id = 'IN-'+ str(id_no.random(length=6))
        check_id = Invoice.objects.filter(id=full_id)

        while(check_id.exists()):
            id_no = shortuuid.ShortUUID(alphabet="0123456789")
            full_id = 'IN-'+ str(id_no.random(length=6))
            check_id = Invoice.objects.filter(id=full_id)

        return full_id

# Invoice Supportive model
class Invoice_Product(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey(Invoice, blank=True, null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(blank=False, null=False, default=0)
    total_price = models.FloatField(blank=False, default=0.0)
    
    def save(self, *args, **kwargs):
        self.total_price = abs(self.quantity) * abs(self.product_id.unit_price)
        super(Invoice_Product, self).save(*args, **kwargs)

