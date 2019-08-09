

from orders.models import OrderInfo,OrderGoods,SKU
from rest_framework import serializers


class OrderSimpleSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(label='创建时间', read_only=True, format="%Y/%m/%d")
    class Meta:
        model = OrderInfo
        fields = ['order_id', 'create_time']


class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['name', 'default_image']


class OrderGoodsSimpleSerializer(serializers.ModelSerializer):
    # 代表的是从表（ordergoods）对象关联的主表对象（sku） --> 一个
    sku = SKUSimpleSerializer()

    class Meta:
        model = OrderGoods
        fields = [
            'count',
            'price',
            'sku'
        ]


class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    # 代表的是与主表对象（orderinfo）关联的所有的从表对象（ordergoods）
    skus = OrderGoodsSimpleSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = "__all__"