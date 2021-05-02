from rest_framework import serializers

from .models import ConfirmationCode


class ConfirmationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ConfirmationCode
