from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'email',
            'bio',
            'role',
            'first_name',
            'last_name'
        )
        model = User
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


class UserSerializerNoRole(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'email',
            'bio',
            'first_name',
            'last_name'
        )
        model = User
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
