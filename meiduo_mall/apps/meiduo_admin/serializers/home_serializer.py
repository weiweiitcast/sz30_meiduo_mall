
# 定义一个序列化器，完成对GoodsVisitCount模型类的序列化操作
# category和count两个字段

from rest_framework import serializers
from goods.models import GoodsVisitCount

class GoodsVisitCountSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = GoodsVisitCount
        fields = ['category', 'count']