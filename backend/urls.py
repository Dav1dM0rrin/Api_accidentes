from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    path("autenticacion/", include("autenticacion.urls"))
]
