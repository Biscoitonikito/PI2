from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class ProfilePostPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1

class PostCommentPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4
