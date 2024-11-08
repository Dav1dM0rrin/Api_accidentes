from accidente.models import *
import django_filters


class BarrioFilter(django_filters.FilterSet):
    barrio = django_filters.CharFilter(field_name="nombre", lookup_expr="iexact")
    zona = django_filters.CharFilter(field_name="zona__nombre", lookup_expr="icontains")


class AccidenteFilter(django_filters.FilterSet):
    fecha = django_filters.DateFilter(field_name="fecha", lookup_expr="exact")
    zona = django_filters.CharFilter(field_name="ubicacion__barrio__zona__nombre", lookup_expr="icontains")
    barrio = django_filters.CharFilter(field_name="ubicacion__barrio__nombre", lookup_expr="icontains")

    sexo_victima = django_filters.CharFilter(field_name="sexo_victima", lookup_expr="exact")
    edad_victima = django_filters.RangeFilter(field_name="edad_victima")

    condicion_victima = django_filters.CharFilter(field_name="condicion_victima__rol_victima", lookup_expr="icontains")
    gravedad_victima = django_filters.CharFilter(field_name="gravedad_victima__nivel_gravedad", lookup_expr="icontains")
    tipo_accidente = django_filters.CharFilter(field_name="tipo_accidente__tipo", lookup_expr="icontains")

    primer_via_tipo_via = django_filters.CharFilter(field_name="ubicacion__primer_via__tipo_via__nombre", lookup_expr="icontains")
    primer_via_numero = django_filters.CharFilter(field_name="ubicacion__primer_via__numero_via", lookup_expr="icontains")
    primer_via_nombre = django_filters.CharFilter(field_name="ubicacion__primer_via__nombre_via", lookup_expr="icontains")
    primer_via_sufijo = django_filters.CharFilter(field_name="ubicacion__primer_via__sufijo_via", lookup_expr="icontains")

    segunda_via_tipo_via = django_filters.CharFilter(field_name="ubicacion__segunda_via__tipo_via__nombre", lookup_expr="icontains")
    segunda_via_numero = django_filters.CharFilter(field_name="ubicacion__segunda_via__numero_via", lookup_expr="icontains")
    segunda_via_nombre = django_filters.CharFilter(field_name="ubicacion__segunda_via__nombre_via", lookup_expr="icontains")
    segunda_via_sufijo = django_filters.CharFilter(field_name="ubicacion__segunda_via__sufijo_via", lookup_expr="icontains")
