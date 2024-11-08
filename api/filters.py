from accidente.models import *
import django_filters


class TipoViaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name="nombre", lookup_expr="iexat")


class ZonaFilter(django_filters.FilterSet):
    zona = django_filters.CharFilter(field_name="nombre", lookup_expr="icontains")


class BarrioFilter(django_filters.FilterSet):
    barrio = django_filters.CharFilter(field_name="nombre", lookup_expr="iexact")
    zona = django_filters.CharFilter(field_name="zona__nombre", lookup_expr="icontains")

    class Meta:
        model = Barrio
        fields = [
            'barrio',
            'zona',
        ]


class AccidenteFilter(django_filters.FilterSet):
    fecha = django_filters.DateFilter(field_name="fecha", lookup_expr="exact")
    zona = django_filters.CharFilter(field_name="ubicacion__barrio__zona__nombre", lookup_expr="iexact")
    barrio = django_filters.CharFilter(field_name="ubicacion__barrio__nombre", lookup_expr="iexact")

    sexo_victima = django_filters.CharFilter(field_name="sexo_victima", lookup_expr="exact")
    edad_victima = django_filters.RangeFilter(field_name="edad_victima")

    condicion_victima = django_filters.CharFilter(field_name="condicion_victima__rol_victima", lookup_expr="iexact")
    gravedad_victima = django_filters.CharFilter(field_name="gravedad_victima__nivel_gravedad", lookup_expr="iexact")
    tipo_accidente = django_filters.CharFilter(field_name="tipo_accidente__tipo", lookup_expr="iexact")

    primer_via_tipo_via = django_filters.CharFilter(field_name="ubicacion__primer_via__tipo_via__nombre", lookup_expr="iexact")
    primer_via_numero = django_filters.CharFilter(field_name="ubicacion__primer_via__numero_via", lookup_expr="iexact")
    primer_via_nombre = django_filters.CharFilter(field_name="ubicacion__primer_via__nombre_via", lookup_expr="iexact")
    primer_via_sufijo = django_filters.CharFilter(field_name="ubicacion__primer_via__sufijo_via", lookup_expr="iexact")

    segunda_via_tipo_via = django_filters.CharFilter(field_name="ubicacion__segunda_via__tipo_via__nombre", lookup_expr="iexact")
    segunda_via_numero = django_filters.CharFilter(field_name="ubicacion__segunda_via__numero_via", lookup_expr="iexact")
    segunda_via_nombre = django_filters.CharFilter(field_name="ubicacion__segunda_via__nombre_via", lookup_expr="iexact")
    segunda_via_sufijo = django_filters.CharFilter(field_name="ubicacion__segunda_via__sufijo_via", lookup_expr="iexact")

    class Meta:
        model = Accidente
        fields = [
            'fecha',
            'zona',
            'barrio',
            'sexo_victima',
            'edad_victima',
            'condicion_victima',
            'gravedad_victima',
            'tipo_accidente',
            'primer_via_tipo_via',
            'primer_via_numero',
            'primer_via_nombre',
            'primer_via_sufijo',
            'segunda_via_tipo_via',
            'segunda_via_numero',
            'segunda_via_nombre',
            'segunda_via_sufijo',
        ]