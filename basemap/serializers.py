from rest_framework import serializers

from person.models import User
from person.serializers import UserSerializer
from .models import BaseMap


class BaseMapSerializer(serializers.ModelSerializer):
    # user=UserSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, allow_null=True)

    class Meta:
        model = BaseMap
        fields = ('name', 'url','user')
