from rest_framework.serializers import ModelSerializer, CharField

from core.models import Advert


class AdvertSerializer(ModelSerializer):
    # default city is city__id because city is catalog and we use redis
    
    # uncomment this if need just city name
    city = CharField(source='city.name')
    owner = CharField(source='owner.email')

    class Meta:
        model = Advert
        fields = (
            'id', 'header', 'description',
            'city', 'owner', 
        )
        read_only_fields = (
            'id', 'city', 
            'owner',
        )
