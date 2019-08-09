
# 定义一个序列化器，完成对GoodsVisitCount模型类的序列化操作
# category和count两个字段

from rest_framework import serializers
from goods.models import GoodsVisitCount

class GoodsVisitCountSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = GoodsVisitCount
        fields = ['category', 'count']








# url请求：/books/1/2/3
# django路由分发，模块会提取路径参数
# 1、命名分组: /books/(?P<a>\d+)/(?P<b>\d+)/(?P<c>\d+)/
#       self.kwargs = {"a":1, "b":2, "c":3}

# 2、匿名分组: # /books/(\d+)/(\d+)/(\d+)/
#       self.args = (1,2,3)

# 调用视图处理此次请求
# self.get(request, *self.args, **self.kwargs)
# 名分分组：self.get(request, *(,), **{"a":1, "b":2, "c":3})
#     --> self.get(request, a=1, b=2, c=3)

# 匿名分组：self.get(request, *(1,2,3), **{})
#     --> self.get(request, 1,2,3)

# django定义url路由映射的时候，如果路径中有参数，可以通过分组的方式提取
# 两种：匿名分组，命名分组
# 要么使用匿名分组，要么使用命名分组，二者不能"共存"： /books/(?P<a>\d+)/(\d+)/ --> 是一个可怕的正则
# 如果二者存在，那么只会提取命名分组参数： self.kwargs = {"a":1};  self.args = (,)
# /books/(?P<a>\d+)/(\d+)/ -->  /books/1/2/ --> self.get(request, a=1)

# class MyView(APIView):
    # 视图函数
    # def get(self, a, b, c):
    #     pass