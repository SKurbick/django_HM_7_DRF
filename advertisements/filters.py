from django_filters import rest_framework as filters
from django_filters.rest_framework import DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    print(" вызван класс просмотра по дате")

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['created_at']

# class MetricFilter(FilterSet):
#     created_at = DateFromToRangeFilter()
#     print(" вызван класс просмотра по дате")
#
#     class Meta:
#         model = Advertisement
#         fields = ['created_at']
