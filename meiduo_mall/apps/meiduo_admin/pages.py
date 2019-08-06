
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class MyPage(PageNumberPagination):
    page_query_param = "page"
    max_page_size = 10
    page_size_query_param = "pagesize"
    page_size = 5

    def get_paginated_response(self, data):
        """
        构建响应对象，构建返回对数据格式
        :param data: 分页的子集
        :return: 响应对象
        """

        return Response({
            "counts": self.page.paginator.count, # 总数量,
            "lists": data,
            "page": self.page.number, # 当前页数
            "pages": self.page.paginator.num_pages, # 总页数
            "pagesize": self.page_size,
        })