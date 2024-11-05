from django.contrib.auth.models import AbstractUser
from backend.base_models import Models
from django.db import models


class Rol(Models):
    nombre = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    primer_nombre = models.CharField(max_length=50, null=False)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    primer_apellido = models.CharField(max_length=50, null=False)
    segundo_apellido = models.CharField(max_length=50, null=False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)

    @staticmethod
    def formatear_username(primer_apellido, segundo_apellido, primer_nombre, segundo_nombre=None):
        if segundo_nombre is None:
            username = f"{segundo_apellido}{primer_apellido}{primer_nombre}"
        else:
            username = f"{segundo_apellido}{primer_apellido}{segundo_nombre}{primer_nombre}"

        return username.upper()

    def __str__(self):
        segundo_nombre = self.segundo_nombre if self.segundo_nombre else ""

        return f"{self.primer_nombre} {segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"
