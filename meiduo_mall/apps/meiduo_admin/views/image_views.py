

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from goods.models import SKUImage,SKU
from meiduo_admin.serializers.image_serializer import *
from meiduo_admin.pages import MyPage

class ImageViewSet(ModelViewSet):
    queryset = SKUImage.objects.all()
    serializer_class = ImageSerializer
    pagination_class = MyPage


class SKUSimpleView(ListAPIView):
    queryset = SKU.objects.all()
    serializer_class = SKUSimpleSerializer