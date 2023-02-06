from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["creator__id"]
    #
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        print("вызван")
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            print("VVVVVV")
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        print("RRRRRRRR")
        return []
