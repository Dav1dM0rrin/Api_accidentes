from autenticacion.models import Usuario
from backend.base_models import Models
from django.db import models


# Create your models here.
class Zona(Models):
    nombre = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.nombre


class Barrio(Models):
    nombre = models.CharField(max_length=100, unique=True, null=False)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.zona}"


class TipoVia(Models):
    nombre = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.nombre


class Via(Models):
    tipo_via = models.ForeignKey(TipoVia, on_delete=models.CASCADE)
    numero_via = models.CharField(max_length=15, null=True, blank=True)
    nombre_via = models.CharField(max_length=50, null=True, blank=True)
    sufijo_via = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        numero_via = str(self.numero_via) if self.numero_via else ""
        nombre_via = str(self.nombre_via) if self.nombre_via else ""
        sufijo_via = str(self.sufijo_via) if self.sufijo_via else ""

        return f"{self.tipo_via} {numero_via} {nombre_via} {sufijo_via}"


class Ubicacion(Models):
    primer_via = models.ForeignKey(Via, on_delete=models.CASCADE, related_name="ubicaciones_primer_via", null=False)
    segunda_via = models.ForeignKey(Via, on_delete=models.CASCADE, related_name="ubicaciones_segunda_via", null=True, blank=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, null=True, blank=True)
    complemento = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['primer_via', 'segunda_via', 'latitud', 'longitud', 'complemento', 'barrio'], name='unique_ubicacion')
        ]

    def __str__(self):
        segunda_via = str(self.segunda_via) if self.segunda_via else ""
        complemento = str(self.complemento) if self.complemento else ""

        return f"#{self.id} - {self.primer_via} {segunda_via} - {self.latitud} | {self.longitud} - {self.barrio} - {complemento}"


class CondicionVictima(Models):
    rol_victima = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return f"{self.rol_victima}"


class GravedadVictima(Models):
    nivel_gravedad = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return f"{self.nivel_gravedad}"


class TipoAccidente(Models):
    tipo = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return f"{self.tipo}"


class Accidente(Models):
    fecha = models.DateField(null=False)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    condicion_victima = models.ForeignKey(CondicionVictima, on_delete=models.CASCADE, null=True)
    gravedad_victima = models.ForeignKey(GravedadVictima, on_delete=models.CASCADE)
    tipo_accidente = models.ForeignKey(TipoAccidente, on_delete=models.CASCADE)
    sexo_victima = models.CharField(max_length=1, null=True, blank=True)
    edad_victima = models.PositiveSmallIntegerField()
    cantidad_victima = models.PositiveSmallIntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha} - {self.ubicacion} - {self.condicion_victima} - {self.gravedad_victima} - {self.cantidad_victima} - {self.sexo_victima} - {self.edad_victima} - Edad {self.edad_victima}"
