from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from api.serializer import AccidenteSerializer
from api.filters import AccidenteFilter
from accidente.models import Accidente
from rest_framework import viewsets


class AccidentePagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    min_page_size = 1
    max_page_size = 50

    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param, self.page_size)

        try:
            page_size = int(page_size)
        except (ValueError, TypeError):
            page_size = self.page_size

        page_size = max(self.min_page_size, min(page_size, self.max_page_size))

        return page_size


class AccidenteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accidente.objects.all().order_by("-id")
    serializer_class = AccidenteSerializer
    pagination_class = AccidentePagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AccidenteFilter
