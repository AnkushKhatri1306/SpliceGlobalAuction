from rest_framework import  serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='id')
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')

    class Meta:
        model = User
        fields = ('user_id', 'firstName', 'lastName', 'email')