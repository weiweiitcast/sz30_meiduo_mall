


from rest_framework import serializers
from django.contrib.auth.models import Group


class GroupSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

    # def create(self, validated_data):
    #     # 手动使用ManyToManyField字段，实现创建中间表数据
    #
    #     # permissions = [78, 79]
    #     permissions = validated_data.pop("permissions")
    #
    #     # 1、新建的分组对象先创建
    #     instance = self.Meta.model.objects.create(**validated_data)
    #     # 2、创建中间表数据
    #     # instance.permissions = permissions # [78, 79]
    #     instance.permissions.set(permissions) # [78, 79]
    #     instance.save()
    #
    #     return instance
