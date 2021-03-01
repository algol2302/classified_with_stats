from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache import caches

from core.models import City
from core.api.serializers import CitySerializer


class CityAPI(ModelViewSet):
    queryset = City.objects.get_queryset()
    serializer_class = CitySerializer

    @method_decorator(
        cache_page(settings.CACHES['city']['TIMEOUT'], cache='city')
    )
    def list(self, request, format=None):
        return super(CityAPI, self).list(self, request, format=None)
