

from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'mobile',

            'password',
            'groups',
            'user_permissions'
        ]

        extra_kwargs = {
            "password": {"write_only": True}
        }


    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        attrs['is_staff'] = True
        return attrs