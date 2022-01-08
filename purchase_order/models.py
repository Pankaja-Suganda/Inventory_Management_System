from django.db import models
from django.db.models import Sum
import datetime
import shortuuid
from supplier.models import Supplier
from materials.models import Materials
from authentication.models import BaseUser


# PO Model
class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        (0, 'Issued'),
        (1, 'Paid'),
        (2, 'Received'),
        (3, 'Closed')
    )

    id = models.CharField(max_length=11, primary_key=True, blank=False)
    user_id = models.ForeignKey(BaseUser, blank=True, null=True, on_delete=models.SET_NULL)
    supplier_id = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.SET_NULL)
    material_ids = models.ManyToManyField('CMaterial', blank=True )
    total_price = models.FloatField(blank=False, default=0.0)
    sub_total_price = models.FloatField(blank=False, default=0.0)
    discount_persentage = models.FloatField(blank=False, default=0.0)
    tax_rate = models.FloatField(blank=False, default=0.0)
    issued_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)
    Received_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    po_pdf = models.FileField(null=True, blank=True, upload_to='core/static/assets/documents/sales order/')
    description = models.TextField(blank=True)

    def get_id(self):
        return self.id

    def class_name(self):
        return self.__class__.__name__
    
    def save(self, *args, **kwargs):
        
        if self.status == 0:
            self.sub_total_price = 0
            self.total_price = 0
            # calculations
            for material in self.material_ids.all():
                self.sub_total_price += material.total_price
            self.total_price = self.sub_total_price - (self.sub_total_price*(self.discount_persentage/100))

            # supplier po count increment
            self.supplier_id.po_count += 1
            # assigning supplier last po date
            self.supplier_id.last_order_date = self.issued_date
            self.supplier_id.save()

        super(PurchaseOrder, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # decrease the po_count of the supplier 
        self.supplier_id.po_count -= 1
        self.supplier_id.save()

        if self.status == 2:
            for cmaterial in self.material_ids.all():
                material = cmaterial.material_id
                material.quatity -= cmaterial.quantity
                material.save()
                material.make_stock_status()
                material.save()
        super(PurchaseOrder, self).delete(*args, **kwargs)
    
    @staticmethod
    def po_id():
        id_no = shortuuid.ShortUUID(alphabet="0123456789")
        full_id = 'PO-'+ str( id_no.random(length=8))
        check_id = PurchaseOrder.objects.filter(id=full_id)

        while(check_id.exists()):
            id_no = shortuuid.ShortUUID(alphabet="0123456789")
            full_id = 'PO-'+ str( id_no.random(length=8))
            check_id = PurchaseOrder.objects.filter(id=full_id)

        return full_id

# PO Supportive model
class CMaterial(models.Model):
    id = models.AutoField(primary_key=True)
    po_id = models.ForeignKey(PurchaseOrder, blank=True, null=True, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Materials, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(blank=False, null=False, default=0)
    total_price = models.FloatField(blank=False, default=0.0)
    
    def save(self, *args, **kwargs):
        self.total_price = abs(self.quantity) * abs(self.material_id.unit_price)
        super(CMaterial, self).save(*args, **kwargs)
