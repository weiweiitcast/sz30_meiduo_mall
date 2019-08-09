

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from goods.models import SpecificationOption
from meiduo_admin.serializers.option_serializer import *
from meiduo_admin.pages import MyPage
from goods.models import SPUSpecification


class OptionViewSet(ModelViewSet):
    queryset = SpecificationOption.objects.all()
    serializer_class = OptSerializer
    pagination_class = MyPage



class OptSpecView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = OptSpecSimpleSerializer