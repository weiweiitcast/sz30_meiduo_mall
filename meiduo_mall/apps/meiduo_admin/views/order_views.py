

from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView
from orders.models import OrderInfo
from meiduo_admin.serializers.order_serializer import *
from meiduo_admin.pages import MyPage


class OrderView(ListAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderSimpleSerializer
    pagination_class = MyPage

    def get_queryset(self):
        keyword = self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(order_id__contains=keyword)
        return self.queryset.all()


class OrderDetailView(RetrieveAPIView, UpdateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderDetailSerializer