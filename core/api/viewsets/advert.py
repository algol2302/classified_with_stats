from rest_framework.viewsets import ModelViewSet

from core.models import Advert
from core.api.serializers import AdvertSerializer

from core.services import click_handler


class AdvertAPI(ModelViewSet):
    serializer_class = AdvertSerializer
    
    def get_queryset(self):
        queryset = Advert.objects.prefetch_related(
            'city',
            'owner',
        ).distinct()
        
        return queryset

    # @method_decorator(
    #     cache_page(settings.CACHES['advert']['TIMEOUT'], cache='advert')
    # )
    def list(self, request, format=None):
        return super(AdvertAPI, self).list(self, request, format=None)

    def retrieve(self, request, pk=None):
        click_handler(advert=self.get_object(), request=request)
        return super(AdvertAPI, self).retrieve(self, request, pk=None)
