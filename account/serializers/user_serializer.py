from rest_framework import serializers

from account.models import User

__all__ = ['UserSerializer']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'user_name', 'phone_number', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }
