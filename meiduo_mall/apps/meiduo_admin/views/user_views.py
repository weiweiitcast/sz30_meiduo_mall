
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from users.models import User
from meiduo_admin.serializers.user_serializer import UserDetailSerializer
from meiduo_admin.pages import MyPage


class UserAPIView(ListAPIView, CreateAPIView):
    # 超级管理员
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserDetailSerializer
    # 指明分页器
    pagination_class = MyPage


    def get_queryset(self):
        # 如果前端传来了keyword，我就过滤
        # 否则默认返回默认的所有的数据集
        keyword = self.request.query_params.get('keyword')
        if keyword:
            return self.queryset.filter(username__contains=keyword)
        # .all():  使用QuerySet集合的缓存
        return self.queryset.all()