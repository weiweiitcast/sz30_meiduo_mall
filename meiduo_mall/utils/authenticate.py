from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest
import re
from users.models import User
from django.utils import timezone

class MeiduoModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        自定义认证流程
        :param request: 请求对象
        :param username: 用户名
        :param password: 密码
        :param kwargs: 额外参数
        :return: 返回None表示认证失败，返回User对象表明认证成功(对应的权限：IsAuthentication)
        """

        try:

            user = User.objects.get(username=username)
        except:
            # 如果未查到数据，则返回None，用于后续判断
            try:
                user = User.objects.get(mobile=username)
            except:
                return None


        # 如果该请求是来自后台管理站点的登陆请求
        # 那么就需要验证用户是否是超级管理员
        # 关键问题：根据request对象是否为空，来判断此次登陆请求是否是后台站点登陆
        if request is None:
            # 后台站点登陆
            if not user.is_staff:
                return None


        # 判断密码
        if user.check_password(password):
            return user
        else:
            return None

