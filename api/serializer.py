from rest_framework import serializers
from accidente.models import *


class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = ("id", "nombre")


class BarrioSerializer(serializers.ModelSerializer):
    zona = ZonaSerializer(read_only=True)

    class Meta:
        model = Barrio
        fields = ("id", "nombre", "zona")


class TipoViaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVia
        fields = ("id", "nombre")


class ViaSerializer(serializers.ModelSerializer):
    tipo_via = TipoViaSerializer(read_only=True)

    class Meta:
        model = Via

        fields = (
            "id",
            "tipo_via",
            "numero_via",
            "nombre_via",
            "sufijo_via",
        )


class UbicacionSerializer(serializers.ModelSerializer):
    primer_via = ViaSerializer(read_only=True)
    segunda_via = ViaSerializer(read_only=True)
    barrio = BarrioSerializer(read_only=True)

    class Meta:
        model = Ubicacion

        fields = (
            "id",
            "primer_via",
            "segunda_via",
            "latitud",
            "longitud",
            "barrio",
            "complemento",
        )


class CondicionVictimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicionVictima
        fields = ("id", "rol_victima")


class GravedadVictimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GravedadVictima
        fields = ("id", "nivel_gravedad")


class TipoAccidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAccidente
        fields = ("id", "tipo")


class AccidenteSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer(read_only=True)
    condicion_victima = CondicionVictimaSerializer(read_only=True)
    gravedad_victima = GravedadVictimaSerializer(read_only=True)
    tipo_accidente = TipoAccidenteSerializer(read_only=True)

    class Meta:
        model = Accidente

        fields = (
            "id",
            "fecha",
            "ubicacion",
            "condicion_victima",
            "gravedad_victima",
            "tipo_accidente",
            "sexo_victima",
            "edad_victima",
            "cantidad_victima",
            "usuario"
        )
