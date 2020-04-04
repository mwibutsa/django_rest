from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationWithUppperBound(LimitOffsetPagination):
    max_limit = 8
