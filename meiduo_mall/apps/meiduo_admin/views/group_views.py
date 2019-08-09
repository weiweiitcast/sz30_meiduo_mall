


from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import Group,Permission
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.group_serializer import *
from meiduo_admin.serializers.perm_serializer import PermSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSimpleSerializer
    pagination_class = MyPage




class PermSimpleView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermSerializer


