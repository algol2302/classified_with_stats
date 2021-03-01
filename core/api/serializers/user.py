from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')