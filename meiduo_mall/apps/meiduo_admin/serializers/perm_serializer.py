

from rest_framework import serializers
from django.contrib.auth.models import Permission,ContentType


class PermSerializer(serializers.ModelSerializer):
    # content_type = serializers.StringRelatedField()

    # PrimaryKeyRelatedField可以作用于序列化（序列化成主键），也可以作用于反序列化（前端来主键，根据主键找到主表对象）
    # content_type = serializers.PrimaryKeyRelatedField(queryset=ContentType.objects.all())
    class Meta:
        model = Permission
        fields = [
            'id',
            'name',
            'codename',
            'content_type'
        ]


class PermContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = [
            'id',
            'name'
        ]