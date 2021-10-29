from django.db import models
import shortuuid
from supplier.models import Supplier
from materials.models import Materials
from authentication.models import BaseUser

# PO Supportive model
class CMaterial(models.Model):
    id = models.AutoField(primary_key=True)
    material_id = models.ForeignKey(Materials, blank=True, null=True, on_delete=models.SET_NULL)
    quatity = models.IntegerField( blank=False, default=0)

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
    material_ids = models.ManyToManyField(CMaterial, blank=True, null=True)
    total_price = models.FloatField(blank=False, default=0.0)
    sub_total_price = models.FloatField(blank=False, default=0.0)
    discount_persentage = models.FloatField(blank=False, default=0.0)
    tax_rate = models.FloatField(blank=False, default=0.0)
    issued_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)
    Received_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    po_pdf = models.FileField(null=True, blank=False, upload_to='core/static/assets/documents/purchase order/')

    def get_id(self):
        return self.id

    def class_name(self):
        return self.__class__.__name__
    
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