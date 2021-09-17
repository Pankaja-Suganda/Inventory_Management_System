import django_filters
from .models import Supplier

class SupplierFilter(django_filters.FilterSet):
    
    class Meta:
        model = Supplier
        fields = ['id', 'company', 'po_count']