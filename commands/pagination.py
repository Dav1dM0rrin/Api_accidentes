from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size_query_param = "page_size"

    def __init__(self, page_size=5, max_page_size=10, min_page_size=1):
        self.page_size = page_size
        self.max_page_size = max_page_size
        self.min_page_size = min_page_size

    def get_page_size(self, request):
        page_size = request.query_params.get("page_size", self.page_size)

        try:
            page_size = int(page_size)
        except (ValueError, TypeError):
            page_size = self.page_size

        page_size = max(self.min_page_size, min(page_size, self.max_page_size))

        return page_size
