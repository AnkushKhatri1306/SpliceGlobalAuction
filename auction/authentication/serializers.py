from rest_framework import  serializers
from .models import *
from auction.config import *

class UserProfileDetailsSerializer(serializers.ModelSerializer):
    userType = serializers.SerializerMethodField()

    class Meta:
        model = UserProfileDetails
        fields = ('userType',)

    def get_userType(self, obj):
        user_type = ''
        try:
            user_type = DEFAULT_USER_TYPE.get(obj.user_type, '')
        except Exception as e:
            print(e.args)
        return user_type