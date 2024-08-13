from rest_framework.pagination import PageNumberPagination


class ModulesPaginator(PageNumberPagination):
    page_size = 2
