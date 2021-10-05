# from django.db import models

# # stock_item Model
# class Stock(models.Model):
#     STATUS_CHOICES = (
#         (0, 'In Stock'),
#         (1, 'Out Stock'),
#     )

#     id = models.CharField(max_length=12, primary_key=True, blank=False)
#     name = models.CharField( max_length=150, blank=False)
#     description = models.CharField( max_length=500, blank=False)
#     unit_price =models.FloatField(blank=False)
#     quatity = models.IntegerField( blank=False, default=0)
#     stock_margin = models.IntegerField( blank=False, default=0)
#     status = models.IntegerField(choices=STATUS_CHOICES, default=0)
#     # category_id = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.SET_NULL)
#     # shell_id = models.ForeignKey(Shell, blank=True, null=True, on_delete=models.SET_NULL)
#     # supplier_id = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.SET_NULL)
#     # user_id = models.ForeignKey(BaseUser, blank=True, null=True, on_delete=models.SET_NULL)

#     def make_stock_status(self):
#         if self.quatity > self.stock_margin:
#             self.status = 0
#         else:
#             self.status = 1

#     @staticmethod
#     def Material_id():
#         id_no = shortuuid.ShortUUID(alphabet="0123456789")
#         full_id = 'M'+ str( id_no.random(length=6))
#         check_id = Materials.objects.filter(id=full_id)

#         while(check_id.exists()):
#             id = shortuuid.ShortUUID(alphabet="0123456789")
#             full_id = 'M'+ str( id.random(length=6))
#             check_id = Materials.objects.filter(id=full_id)

#         return full_id

#     def class_name(self):
#         return self.__name__

#     class Meta:
#         __name__ = 'Materials'

# # Category Model
# class Categories(models.Model):
#     id = models.CharField(max_length=7, primary_key=True, blank=False)
#     name = models.CharField( max_length=150, blank=False)
#     description = models.CharField( max_length=350, blank=False)

#     def class_name(self):
#         return self.__name__

#     @staticmethod
#     def category_id():
#         id_no = shortuuid.ShortUUID(alphabet="0123456789")
#         full_id = 'CAT'+ str( id_no.random(length=4))
#         check_id = Categories.objects.filter(id=full_id)

#         while(check_id.exists()):
#             id = shortuuid.ShortUUID(alphabet="0123456789")
#             full_id = 'CAT'+ str( id.random(length=4))
#             check_id = Categories.objects.filter(id=full_id)

#         return full_id
    
#     class Meta:
#         __name__ = 'Categories'

# # size Model
# class Size(models.Model):
#     id = models.CharField(max_length=7, primary_key=True, blank=False)
#     name = models.CharField( max_length=150, blank=False)
#     description = models.CharField( max_length=350, blank=False)

#     def class_name(self):
#         return self.__name__

#     @staticmethod
#     def category_id():
#         id_no = shortuuid.ShortUUID(alphabet="0123456789")
#         full_id = 'CAT'+ str( id_no.random(length=4))
#         check_id = Categories.objects.filter(id=full_id)

#         while(check_id.exists()):
#             id = shortuuid.ShortUUID(alphabet="0123456789")
#             full_id = 'CAT'+ str( id.random(length=4))
#             check_id = Categories.objects.filter(id=full_id)

#         return full_id
    
#     class Meta:
#         __name__ = 'Categories'
