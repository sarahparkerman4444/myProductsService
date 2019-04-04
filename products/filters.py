from django_filters import rest_framework as filters

from products.models import Product


class ProductFilter(filters.FilterSet):
    workflowlevel2_uuid = filters.BaseInFilter()

    class Meta:
        model = Product
        fields = ('type', 'name', 'workflowlevel2_uuid', 'part_number', )
