"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from meiduo_admin.views.login_view import LoginAPIView
from rest_framework_jwt.views import obtain_jwt_token
from meiduo_admin.views.home_view import *
from rest_framework.routers import SimpleRouter

urlpatterns = [
    # 手动实现登陆视图和序列化器
    # url(r'^authorizations/$', LoginAPIView.as_view()),
    # 使用第三方提供的用于构建返回token值的视图接口完成签发
    # obtain_jwt_token视图最终返回的结果只有token值
    url(r'^authorizations/$', obtain_jwt_token),
    # url(r'^statistical/total_count/$', UserTotalCount.as_view()),
    # url(r'^statistical/day_increment/$', UserDayIncreView.as_view()),
    # url(r'^statistical/day_active/$', UserActiveView.as_view()),
    # url(r'^statistical/day_orders/$', UserOrderView.as_view()),
    # url(r'^statistical/month_increment/$', UserMonthIncrView.as_view()),

    url(r'^statistical/goods_day_views/$', GoodsVisitCountView.as_view()),
]


router = SimpleRouter()
router.register(prefix='statistical', viewset=HomeViewSet, base_name='home')
urlpatterns += router.urls













