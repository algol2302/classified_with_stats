from rest_framework.serializers import ModelSerializer

from core.models import City


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name',)
