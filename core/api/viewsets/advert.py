from infi.clickhouse_orm import Database

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache import caches

from core.models import Advert, CustomUser
from core.api.serializers import AdvertSerializer
from clicks.models import Clicks

db = Database('demo')


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
        # TODO move all logic to service layers from views
        obj = self.get_object()
        # TODO add IP to Clicks
        # ip = request.META['REMOTE_ADDR']
        
        try:
            user = CustomUser.objects.get(id=self.request.user)
        except:
            user = CustomUser.objects.get(email='anonymous@anonymous.an')

        db.insert([
            Clicks(
                advert_id=obj.id, advert_owner_id=obj.owner_id, advert_city_id=obj.city_id, visitor_id=user.id
            )
        ])

        return super(AdvertAPI, self).retrieve(self, request, pk=None)
