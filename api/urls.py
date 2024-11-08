from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r"tipo_vias", views.ZonaViewSet, basename="tipo_via")
router.register(r"zonas", views.ZonaViewSet, basename="zona")
router.register(r"barrios", views.BarrioViewSet, basename="barrio")
router.register(r"accidentes", views.AccidenteViewSet, basename="accidente")


urlpatterns = [
    path("", include(router.urls))
]