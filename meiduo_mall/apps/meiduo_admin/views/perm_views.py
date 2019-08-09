

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import Permission,ContentType
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.perm_serializer import *
from rest_framework.decorators import action


class PermViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermSerializer
    pagination_class = MyPage

    def get_queryset(self):
        if self.action == "content_types":
            return ContentType.objects.all()
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == "content_types":
            return PermContentTypeSerializer
        return self.serializer_class


    @action(methods=['get'], detail=False)
    def content_types(self, request):
        # 序列化返回所有权限的可选类型数据
        content_typeset = self.get_queryset()
        serializer = self.get_serializer(content_typeset, many=True)
        return Response(serializer.data)
