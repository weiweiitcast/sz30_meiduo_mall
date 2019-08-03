from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token
from meiduo_admin.views.login_views import *


urlpatterns = [
    # 登陆请求，签发token
    # url(r'^authorizations/$', LoginView.as_view()),
    url(r'^authorizations/$', obtain_jwt_token),
]