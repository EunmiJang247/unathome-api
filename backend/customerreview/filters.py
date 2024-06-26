from django_filters import rest_framework as filters
from .models import Customerreview


class CustomerreviewFilter(filters.FilterSet):
    min_size = filters.NumberFilter(field_name="size", lookup_expr='gte')
    max_size = filters.NumberFilter(field_name="size", lookup_expr='lte')

    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Customerreview
        fields = ('residentType', 'onAds', 'min_price', 'max_price', 'min_size', 'max_size')
