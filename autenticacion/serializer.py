from autenticacion.models import Usuario
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = Usuario

        fields = [
            "id",
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "email",
            "password"
        ]
