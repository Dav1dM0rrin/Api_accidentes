from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    primer_nombre = models.CharField(max_length=50, null=False)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    primer_apellido = models.CharField(max_length=50, null=False)
    segundo_apellido = models.CharField(max_length=50, null=False)

    @classmethod
    def existe(cls, username):
        return cls.objects.filter(username=username).exists()

    @classmethod
    def email_existe(cls, email):
        return cls.objects.filter(email=email).exists()

    @staticmethod
    def formatear_username(primer_apellido, segundo_apellido, primer_nombre, segundo_nombre=None):
        if segundo_nombre is None:
            username = f"{segundo_apellido}{primer_apellido}{primer_nombre}"
        else:
            username = f"{segundo_apellido}{primer_apellido}{segundo_nombre}{primer_nombre}"

        return username.upper()

