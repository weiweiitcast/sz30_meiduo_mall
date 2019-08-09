


from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from users.models import User
from django.contrib.auth.models import Group
from meiduo_admin.serializers.admin_serializer import *
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.group_serializer import GroupSimpleSerializer


class AdminUserViewSet(ModelViewSet):
    # 超级管理员
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminUserSerializer
    pagination_class = MyPage


class GroupSimpleView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSimpleSerializer
