from rest_framework import serializers
from .models import User, UserProfile
from car.serializers import CarSerializer
# from basemap.serializers import BaseMapSerializer
from car.models import Car
from basemap.models import BaseMap


class UserSerializer(serializers.ModelSerializer):
    Car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=True, allow_null=True)
    basemap = serializers.PrimaryKeyRelatedField(queryset=BaseMap.objects.all(), many=True, allow_null=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'profile_user', 'basemap', 'Car')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data.get('username'),
    #         first_name=validated_data.get('first_name'),
    #         last_name=validated_data.get('last_name'),
    #         password=validated_data.get('password'),
    #         profile_user=validated_data.get('profile_user'),
    #         # basemap_set=validated_data['basemap'],
    #         # car=validated_data['Car'],
    #     )
    #     user.Car.set(validated_data.get('Car'))
    #     user.basemap.set(validated_data.get('basemap'))
    #     return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('biography', 'position')
