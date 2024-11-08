from django_filters.rest_framework import DjangoFilterBackend
from commands.pagination import Pagination
from accidente.models import Accidente
from rest_framework import viewsets
from api.serializer import *
from api.filters import *


class ZonaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ZonaFilter


class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BarrioFilter


class TipoViaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoVia.objects.all()
    serializer_class = TipoViaSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TipoViaFilter


class AccidenteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accidente.objects.all().order_by("-id")
    serializer_class = AccidenteSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AccidenteFilter
