

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from goods.models import SPU,Brand,GoodsCategory
from meiduo_admin.serializers.spu_serializer import *
from meiduo_admin.pages import MyPage

class SPUViewSet(ModelViewSet):
    queryset = SPU.objects.all()
    serializer_class = SPUDetailSerializer
    pagination_class = MyPage


class BrandSimpleView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSimpleSerializer


class GoodsCategorySimpleView(ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategroySimpleSerializer

    def get_queryset(self):
        # 如果请求的是获得一级分类对象，filter(parent=None)
        # 如果路径中存在pk，那么就是返回根据parent_id=pk过滤出二级或三级分类对象
        parent_id = self.kwargs.get('pk')
        if not parent_id:
            return self.queryset.filter(parent=None)
        return self.queryset.filter(parent_id=parent_id)