from django.urls import path, re_path
from autenticacion import views


urlpatterns = [
    path("registro", views.registro),
    path("login", views.login),
    path("perfil", views.perfil),
]
