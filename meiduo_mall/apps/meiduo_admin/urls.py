from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token
from meiduo_admin.views.login_views import *
from meiduo_admin.views.home_views import *
from meiduo_admin.views.user_views import UserAPIView

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
]

router = SimpleRouter()
router.register(prefix="statistical", viewset=HomeView, base_name="home")
urlpatterns += router.urls