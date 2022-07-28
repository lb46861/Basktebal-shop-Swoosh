import django_filters
from django_filters import CharFilter

from .models import *


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['team_id', 'category_id', 'brand_id']
    


class OrderFilter(django_filters.FilterSet):
    name = CharFilter(field_name='customer_id__email', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['customer_id__email']   

    
