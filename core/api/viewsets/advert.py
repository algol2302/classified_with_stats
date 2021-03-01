from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache import caches

from hitcount.models import Hit, HitCount, HitCountMixin

from core.models import Advert
from core.api.serializers import AdvertSerializer


class AdvertAPI(ModelViewSet):
    serializer_class = AdvertSerializer
    
    def get_queryset(self):
        queryset = Advert.objects.prefetch_related(
            'city',
            'owner',
        ).distinct()
        
        return queryset

    @method_decorator(
        cache_page(settings.CACHES['advert']['TIMEOUT'], cache='advert')
    )
    def list(self, request, format=None):
        return super(AdvertAPI, self).list(self, request, format=None)

    def retrieve(self, request, pk=None):
        obj = self.get_object()
        ip = request.META['REMOTE_ADDR']
        
        try:
            user = User.objects.get(id=self.request.user)
        except:
            user = User.objects.get(username='Anonymous')

        hit, created = Hit.objects.get_or_create(
            ip=ip,
            user=user,
            hitcount=obj.hit_count,
            session='sss',
            user_agent='api',
        )

        if created:
            caches['advert'].clear()
        
        return super(AdvertAPI, self).retrieve(self, request, pk=None)
