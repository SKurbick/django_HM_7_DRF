from django_filters.rest_framework import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class MetricFilter(FilterSet):
    created_at = DateFromToRangeFilter()
    print(" вызван класс просмотра по дате")

    class Meta:
        model = Advertisement
        fields = ['created_at']


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["id", ]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["creator__id"]
    filterset_class = MetricFilter
    throttle_classes = [AnonRateThrottle]

    def get_permissions(self):
        print("вызван")
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
