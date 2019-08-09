from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token
from meiduo_admin.views.login_views import *
from meiduo_admin.views.home_views import *
from meiduo_admin.views.user_views import UserAPIView
from meiduo_admin.views.sku_views import *
from meiduo_admin.views.spu_views import *
from meiduo_admin.views.spec_views import *
from meiduo_admin.views.option_views import *
from meiduo_admin.views.image_views import *
from meiduo_admin.views.order_views import *
from meiduo_admin.views.perm_views import *
from meiduo_admin.views.group_views import *
from meiduo_admin.views.admin_views import *

from rest_framework.routers import SimpleRouter

urlpatterns = [
    # 登陆请求，签发token
    # url(r'^authorizations/$', LoginView.as_view()),
    url(r'^authorizations/$', obtain_jwt_token),

    # url(r'^statistical/total_count/$', HomeView.as_view({"get":"total_count"})),
    # url(r'^statistical/day_increment/$', HomeView.as_view({"get":"day_increment"})),
    # url(r'^statistical/day_active/$', HomeView.as_view({"get":"day_active"})),

    url(r'^statistical/goods_day_views/$', GoodsVisitCountView.as_view()),

    url(r'^users/$', UserAPIView.as_view()),

    url(r'^skus/$', SKUViewSet.as_view({"get":"list", "post":"create"})),

    url(r'^skus/(?P<pk>\d+)/$', SKUViewSet.as_view({"get":"retrieve",
                                                    "put":"update",
                                                    "delete":"destroy"})),

    url(r'^skus/categories/$', SKUCategoryView.as_view()),
    url(r'^goods/simple/$', SPUSimpleView.as_view()),
    url(r'^goods/(?P<pk>\d+)/specs/$', SPUSpecView.as_view()),


    url(r'^goods/$', SPUViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^goods/(?P<pk>\d+)/$', SPUViewSet.as_view({"get":"retrieve",
                                                     "put":"update",
                                                     "delete":"destroy"})),

    url(r'^goods/brands/simple/$', BrandSimpleView.as_view()),

    url(r'^goods/channel/categories/$', GoodsCategorySimpleView.as_view()),
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', GoodsCategorySimpleView.as_view()),


    url(r'^goods/specs/$', SpecViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^goods/specs/(?P<pk>\d+)/$', SpecViewSet.as_view({"get":"retrieve",
                                                            "put":"update",
                                                            "delete":"destroy"})),

    url(r'^specs/options/$', OptionViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^specs/options/(?P<pk>\d+)/$', OptionViewSet.as_view({"delete":"destroy",
                                                                "get":"retrieve",
                                                                "put":"update"})),


    url(r'^goods/specs/simple/$', OptSpecView.as_view()),


    url(r'^skus/images/$', ImageViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^skus/images/(?P<pk>\d+)/$', ImageViewSet.as_view({"get":"retrieve",
                                                             "put":"update",
                                                             "delete":"destroy"})),

    url(r'^skus/simple/$', SKUSimpleView.as_view()),

    url(r'^orders/$', OrderView.as_view()),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetailView.as_view()),
    url(r'^orders/(?P<pk>\d+)/status/$', OrderDetailView.as_view()),


    # 权限处理
    url(r'^permission/perms/$', PermViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^permission/perms/(?P<pk>\d+)/$', PermViewSet.as_view({"get":"retrieve",
                                                                 "put":"update",
                                                                 "delete":"destroy"})),
    # 获取新增权限可选类型
    url(r'^permission/content_types/$', PermViewSet.as_view({"get":"content_types"})),

    # 组管理
    url(r'^permission/groups/$', GroupViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^permission/groups/(?P<pk>\d+)/$', GroupViewSet.as_view({"delete":"destroy",
                                                                   "get":"retrieve",
                                                                   "put":"update"})),
    # 新建分组可选权限
    url(r'^permission/simple/$', PermSimpleView.as_view()),

    # 超级管理员
    url(r'^permission/admins/$', AdminUserViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^permission/admins/(?P<pk>\d+)/$', AdminUserViewSet.as_view({"get":"retrieve",
                                                                       "put":"update",
                                                                       "delete":"destroy"})),
    # 获得新建管理员可选分组
    url(r'^permission/groups/simple/$', GroupSimpleView.as_view()),
]

router = SimpleRouter()

router.register(prefix="statistical", viewset=HomeView, base_name="home")

# SPU
# /goods/(?P<pk>[^/.]+)/  -->  goods/specs/ -->  {"pk": "specs"}
# router.register(prefix='goods', viewset=SPUViewSet, base_name='spu')
# SPEC
# /goods/specs/
# router.register(prefix='goods/specs', viewset=SpecViewSet, base_name='specs')


urlpatterns += router.urls





# from fdfs_client.client import Fdfs_client
# conn = Fdfs_client()
# 上传本地文件
# conn.upload_by_filename('./')
# 上传文件数据
# conn.upload_by_buffer()

