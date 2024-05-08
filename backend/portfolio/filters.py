from django_filters import rest_framework as filters
from .models import Portfolio, Tag, TypeField


class PortfoliosFilter(filters.FilterSet):
    min_size = filters.NumberFilter(field_name="size", lookup_expr='gte')
    max_size = filters.NumberFilter(field_name="size", lookup_expr='lte')

    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    tags = filters.ModelMultipleChoiceFilter(field_name='tags__name', to_field_name='name', queryset=Tag.objects.all())

    residentType = filters.ChoiceFilter(choices=TypeField.choices)
    
    class Meta:
        model = Portfolio
        fields = ('residentType', 'onAds', 'min_price', 'max_price', 'min_size', 'max_size', 'tags')
