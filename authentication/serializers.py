from rest_framework import serializers

from ads.models import User


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
