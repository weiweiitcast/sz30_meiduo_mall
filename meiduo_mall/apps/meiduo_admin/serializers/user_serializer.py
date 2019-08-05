

# 定义一个序列化器，对User进行序列化操作
from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', # read_only=True
            'username',
            'mobile',
            'email',

            'password'
        ]

        extra_kwargs = {
            'password': {"write_only": True}
        }


    def create(self, validated_data):
        """
        新建用户的时候，1、密码加密；2、超级管理员
        :param validated_data:
        :return: 用户对象
        """

        # password = validated_data['password'] # 明文
        # validated_data['password'] = 密文
        # validated_data['password'] = make_password(password)
        # validated_data['is_staff'] = True
        # 有效数据中：1、明文该密文；2、添加is_staff=True
        # return super().create(validated_data)

        return self.Meta.model.objects.create_superuser(**validated_data)













