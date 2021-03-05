from django.conf.urls import include
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from core.api.viewsets import AdvertAPI, CityAPI


router = routers.DefaultRouter()
schema_view = get_schema_view(title='Pastebin API')

router.register('advert', AdvertAPI, basename='advert_request')
router.register('city', CityAPI, basename='city_request')

urlpatterns = [
    # api
    path('', include(router.urls)),
    path('schema/', login_required(schema_view)),
]
