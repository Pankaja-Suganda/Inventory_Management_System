from django.contrib import admin
from .models import Shell, Categories, Materials

# Register your models here.
admin.site.register(Shell)
admin.site.register(Categories)
admin.site.register(Materials)