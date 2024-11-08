from accidente.models import *
from django.db import IntegrityError
from datetime import datetime
import pandas as pd


zonas = [
    Zona(nombre="Suroccidente"),
    Zona(nombre="Suroriente"),
    Zona(nombre="Norte - Centro Histórico"),
    Zona(nombre="Metropolitana"),
    Zona(nombre="Riomar"),
]


def zona_fk(nombre):
    zona, _ = Zona.objects.get_or_create(nombre=nombre)

    return zona


barrios = [
    # Suroccidente
    Barrio(nombre="Alfonso López", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Bernardo Hoyos", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Buena Esperanza", zona=zona_fk("Suroccidente")),
    Barrio(nombre="California", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Caribe Verde", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Carlos Meisel", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Ciudad Modesto", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Ciudadela de la Salud", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Ciudadela de Paz", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Colina Campestre", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Cordialidad", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Corregimiento de Juan Mina", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Cuchilla de Villate", zona=zona_fk("Suroccidente")),
    Barrio(nombre="El Bosque", zona=zona_fk("Suroccidente")),
    Barrio(nombre="El Carmén", zona=zona_fk("Suroccidente")),
    Barrio(nombre="El Eden", zona=zona_fk("Suroccidente")),
    Barrio(nombre="El Pueblo", zona=zona_fk("Suroccidente")),
    Barrio(nombre="El Romance", zona=zona_fk("Suroccidente")),
    Barrio(nombre="El Rubí", zona=zona_fk("Suroccidente")),
    Barrio(nombre="El Silencio", zona=zona_fk("Suroccidente")),
    Barrio(nombre="El Valle", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Evaristo Sourdis", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Gerlein y Villate", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Kalamary", zona=zona_fk("Suroccidente")),
    Barrio(nombre="La Ceiba", zona=zona_fk("Suroccidente")),
    Barrio(nombre="La Esmeralda", zona=zona_fk("Suroccidente")),
    Barrio(nombre="La Florida", zona=zona_fk("Suroccidente")),
    Barrio(nombre="La Gloria", zona=zona_fk("Suroccidente")),
    Barrio(nombre="La Libertad", zona=zona_fk("Suroccidente")),
    Barrio(nombre="La Manga", zona=zona_fk("Suroccidente")),
    Barrio(nombre="La Paz", zona=zona_fk("Suroccidente")),
    Barrio(nombre="La Pradera", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Las Colinas", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Las Estrellas", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Las Malvinas", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Las Terrazas", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Lipaya", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Loma Fresca", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Los Andes", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Los Angeles I", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Los Angeles II", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Los Angeles III", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Los Olivos I", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Los Olivos II", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Los Pinos", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Los Rosales", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Lucero", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Me Quejo", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Mercedes Sur", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Nueva Colombia", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Nueva Granada", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Olaya", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Pinar del Rio", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Por Fin", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Pumarejo", zona=zona_fk("Suroccidente")),
    Barrio(nombre="San Felipe", zona=zona_fk("Suroccidente")),
    Barrio(nombre="San Isidro", zona=zona_fk("Suroccidente")),
    Barrio(nombre="San Pedro Alejandrino", zona=zona_fk("Suroccidente")),
    Barrio(nombre="San Pedro Sector I", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Santo Domigo", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Siete de Agosto", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Villa del Rosario", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Villa Flor", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Villas de la Cordialidad", zona=zona_fk("Suroccidente")),
    Barrio(nombre="Villas de San Pablo", zona=zona_fk("Suroccidente")),

    # Metropolitana
    Barrio(nombre="Buenos Aires", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Carrizal", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Cevillar", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Ciudadela 20 de Julio", zona=zona_fk("Metropolitana")),
    Barrio(nombre="El Santuario", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Kennedy", zona=zona_fk("Metropolitana")),
    Barrio(nombre="La Sierra", zona=zona_fk("Metropolitana")),
    Barrio(nombre="La Sierrita", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Las Americas", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Las Cayenas", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Las Gardenias", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Las Granjas", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Los Continentes", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Los Girasoles", zona=zona_fk("Metropolitana")),
    Barrio(nombre="San Luis", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Santa María", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Santo Domingo de Guzman", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Sevilla Real", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Siete de Abril", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Sinaí", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Veinte de Julio", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Villa San Carlos", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Villa San Pedro", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Villa Sevilla", zona=zona_fk("Metropolitana")),
    Barrio(nombre="Villa Valery", zona=zona_fk("Metropolitana")),

    # Suroriente
    Barrio(nombre="Atlántico", zona=zona_fk("Suroriente")),
    Barrio(nombre="Bellarena", zona=zona_fk("Suroriente")),
    Barrio(nombre="Boyaca", zona=zona_fk("Suroriente")),
    Barrio(nombre="Chiquinquira", zona=zona_fk("Suroriente")),
    Barrio(nombre="El Campito", zona=zona_fk("Suroriente")),
    Barrio(nombre="El Limón", zona=zona_fk("Suroriente")),
    Barrio(nombre="El Milagro", zona=zona_fk("Suroriente")),
    Barrio(nombre="El Parque Sector Barranquilla", zona=zona_fk("Suroriente")),
    Barrio(nombre="José Antonio Galán", zona=zona_fk("Suroriente")),
    Barrio(nombre="La Arboraya", zona=zona_fk("Suroriente")),
    Barrio(nombre="La Chinita", zona=zona_fk("Suroriente")),
    Barrio(nombre="La Luz", zona=zona_fk("Suroriente")),
    Barrio(nombre="La Magdalena", zona=zona_fk("Suroriente")),
    Barrio(nombre="La Unión", zona=zona_fk("Suroriente")),
    Barrio(nombre="La Victoria", zona=zona_fk("Suroriente")),
    Barrio(nombre="Las Dunas", zona=zona_fk("Suroriente")),
    Barrio(nombre="Las Nieves", zona=zona_fk("Suroriente")),
    Barrio(nombre="Las Palmas", zona=zona_fk("Suroriente")),
    Barrio(nombre="Las Palmeras", zona=zona_fk("Suroriente")),
    Barrio(nombre="Los Laureles", zona=zona_fk("Suroriente")),
    Barrio(nombre="Los Trupillos", zona=zona_fk("Suroriente")),
    Barrio(nombre="Moderno", zona=zona_fk("Suroriente")),
    Barrio(nombre="Montes", zona=zona_fk("Suroriente")),
    Barrio(nombre="Pasadena", zona=zona_fk("Suroriente")),
    Barrio(nombre="Primero de Mayo El Ferry", zona=zona_fk("Suroriente")),
    Barrio(nombre="Rebolo", zona=zona_fk("Suroriente")),
    Barrio(nombre="San Jose", zona=zona_fk("Suroriente")),
    Barrio(nombre="San Nicolás", zona=zona_fk("Suroriente")),
    Barrio(nombre="San Roque", zona=zona_fk("Suroriente")),
    Barrio(nombre="Santa Helena", zona=zona_fk("Suroriente")),
    Barrio(nombre="Simón Bolívar", zona=zona_fk("Suroriente")),
    Barrio(nombre="Tayrona", zona=zona_fk("Suroriente")),
    Barrio(nombre="Universal I", zona=zona_fk("Suroriente")),
    Barrio(nombre="Universal II", zona=zona_fk("Suroriente")),
    Barrio(nombre="Villa Blanca", zona=zona_fk("Suroriente")),
    Barrio(nombre="Villa del Carmén", zona=zona_fk("Suroriente")),

    # Norte - Centro Histórico
    Barrio(nombre="Abajo", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Alameda del Rio", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Altos del Prado", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="America", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Barlovento", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Bellavista", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Bethania	", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Bostón", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Campo Alegre", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Centro", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Ciudad Jardín", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Colombia", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="El Castillo", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="El Golf", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="El Porvenir", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="El Prado", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="El Recreo", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="El Rosario", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="El Tabor", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Granadillo", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="La Campiña", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="La Concepción", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="La Cumbre", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="La Loma", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Las Delicias", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Las Mercedes", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Las Nubes (vereda)", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Los Alpes", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Los Jobos", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Los Nogales", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Miramar", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Modelo", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Montecristo", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Nuevo Horizonte", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Paraiso", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="San Francisco", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Santa Ana", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Villa Country", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Villanueva", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Zona Franca", zona=zona_fk("Norte - Centro Histórico")),
    Barrio(nombre="Zona Industrial", zona=zona_fk("Norte - Centro Histórico")),

    # Riomar
    Barrio(nombre="Altamira", zona=zona_fk("Riomar")),
    Barrio(nombre="Altos de Riomar", zona=zona_fk("Riomar")),
    Barrio(nombre="Altos del Limón", zona=zona_fk("Riomar")),
    Barrio(nombre="Andalucia", zona=zona_fk("Riomar")),
    Barrio(nombre="Corregimiento Eduardo Santos La Playa", zona=zona_fk("Riomar")),
    Barrio(nombre="El Limoncito", zona=zona_fk("Riomar")),
    Barrio(nombre="El Poblado", zona=zona_fk("Riomar")),
    Barrio(nombre="La Floresta", zona=zona_fk("Riomar")),
    Barrio(nombre="Las Flores", zona=zona_fk("Riomar")),
    Barrio(nombre="Las Tres Ave Maria", zona=zona_fk("Riomar")),
    Barrio(nombre="Riomar", zona=zona_fk("Riomar")),
    Barrio(nombre="San Salvador", zona=zona_fk("Riomar")),
    Barrio(nombre="San Vicente", zona=zona_fk("Riomar")),
    Barrio(nombre="Santa Mónica", zona=zona_fk("Riomar")),
    Barrio(nombre="Siape", zona=zona_fk("Riomar")),
    Barrio(nombre="Solaire Norte", zona=zona_fk("Riomar")),
    Barrio(nombre="Villa Campestre", zona=zona_fk("Riomar")),
    Barrio(nombre="Villa Carolina", zona=zona_fk("Riomar")),
    Barrio(nombre="Villa del Este", zona=zona_fk("Riomar")),
    Barrio(nombre="Villa Santos", zona=zona_fk("Riomar")),
]


tipo_vias = [
    TipoVia(nombre="CALLE"),
    TipoVia(nombre="CARRERA"),
    TipoVia(nombre="DIAGONAL"),
    TipoVia(nombre="TRANSVERSAL"),
    TipoVia(nombre="AVENIDA"),
    TipoVia(nombre="VIA"),
    TipoVia(nombre="CORREDOR")
]


condiciones_victima = [
    CondicionVictima(rol_victima="Peaton"),
    CondicionVictima(rol_victima="Acompañante"),
    CondicionVictima(rol_victima="Conductor"),
    CondicionVictima(rol_victima="Motociclista"),
    CondicionVictima(rol_victima="Pasajero"),
    CondicionVictima(rol_victima="Ciclista"),
    CondicionVictima(rol_victima="Menor de edad"),
    CondicionVictima(rol_victima="No reporto")
]


gravedades_victima = [
    GravedadVictima(nivel_gravedad="Herido"),
    GravedadVictima(nivel_gravedad="Muerto"),
]


tipos_accidente = [
    TipoAccidente(tipo="Atropello"),
    TipoAccidente(tipo="Choque"),
    TipoAccidente(tipo="Caida Ocupante"),
    TipoAccidente(tipo="Volcamiento"),
    TipoAccidente(tipo="Otro"),
    TipoAccidente(tipo="Incendio"),
]


def llenar_bd():
    Barrio.objects.bulk_create(barrios, batch_size=1000)
    TipoVia.objects.bulk_create(tipo_vias, batch_size=10)
    CondicionVictima.objects.bulk_create(condiciones_victima, batch_size=100)
    GravedadVictima.objects.bulk_create(gravedades_victima, batch_size=100)
    TipoAccidente.objects.bulk_create(tipos_accidente, batch_size=100)


data = pd.read_csv("utils/accidentes.csv")


def llenar_vias_accidentes():
    llenar_bd()

    for index, fila in data.iterrows():
        complemento = fila["COMPLEMENTO"]

        # VIAS
        primer_via_tipo, _ = TipoVia.objects.get_or_create(nombre=fila["1VIA_TIPO"])
        primer_via_numero = fila["1VIA_NUM"]
        primer_via_nombre = fila["1VIA_NOM"]
        primer_via_sufijo = fila["1SUFIJO"]

        primer_via, _ = Via.objects.get_or_create(
            tipo_via=primer_via_tipo,
            numero_via=primer_via_numero if not pd.isna(primer_via_numero) else None,
            nombre_via=primer_via_nombre if not pd.isna(primer_via_nombre) else None,
            sufijo_via=primer_via_sufijo if not pd.isna(primer_via_sufijo) else None,
        )

        # UBICACION
        latitud = fila["LATITUD"] if not pd.isna(fila["LATITUD"]) else None
        longitud = fila["LONGITUD"] if not pd.isna(fila["LONGITUD"]) else None

        zona, _ = Zona.objects.get_or_create(nombre="Sin definir")
        barrio, _ = Barrio.objects.get_or_create(nombre="Sin definir", zona=zona)

        if not pd.isna(fila["2VIA_TIPO"]):
            segunda_via_tipo, _ = TipoVia.objects.get_or_create(nombre=fila["2VIA_TIPO"])
            segunda_via_numero = fila["2VIA_NUM"]
            segunda_via_nombre = fila["2VIA_NOM"]
            segunda_via_sufijo = fila["2SUFIJO"]

            segunda_via, _ = Via.objects.get_or_create(
                tipo_via=segunda_via_tipo,
                numero_via=segunda_via_numero if not pd.isna(segunda_via_numero) else None,
                nombre_via=segunda_via_nombre if not pd.isna(segunda_via_nombre) else None,
                sufijo_via=segunda_via_sufijo if not pd.isna(segunda_via_sufijo) else None,
            )

            filtros_ubicacion = {
                "primer_via": primer_via,
                "segunda_via": segunda_via,
                "latitud": latitud,
                "longitud": longitud,
                "complemento": complemento if not pd.isna(complemento) else None,
                "barrio": barrio,
            }
        else:
            filtros_ubicacion = {
                "primer_via": primer_via,
                "latitud": latitud,
                "longitud": longitud,
                "complemento": complemento if not pd.isna(complemento) else None,
                "barrio": barrio,
            }

        ubicacion_existente = Ubicacion.objects.filter(**filtros_ubicacion).first()

        if ubicacion_existente:
            ubicacion = ubicacion_existente
        else:
            ubicacion = Ubicacion(**filtros_ubicacion)
            ubicacion.save()

        # ACCIDENTE
        fecha = fila["FECHA_ACCIDENTE"]

        condicion_victima = fila["CONDICION_VICTIMA"] if not pd.isna(fila["CONDICION_VICTIMA"]) else None
        gravedad_victima = fila["GRAVEDAD_VICTIMA"] if not pd.isna(fila["GRAVEDAD_VICTIMA"]) else None

        if not pd.isna(fila["CONDICION_VICTIMA"]):
            condicion_victima, _ = CondicionVictima.objects.get_or_create(rol_victima = fila["CONDICION_VICTIMA"])

        if not pd.isna(fila["GRAVEDAD_VICTIMA"]):
            gravedad_victima, _ = GravedadVictima.objects.get_or_create(nivel_gravedad = fila["GRAVEDAD_VICTIMA"])

        if not pd.isna(fila["TIPO_ACCIDENTE"]):
            tipo_accidente, _ = TipoAccidente.objects.get_or_create(tipo = fila["TIPO_ACCIDENTE"])
        else:
            tipo_accidente, _ = TipoAccidente.objects.get_or_create(tipo="Otro")

        sexo_victima = fila["SEXO_VICTIMA"]
        edad_victima = fila["EDAD_VICTIMA"]
        cant_victima = fila["CANTIDAD_VICTIMAS"]

        usuario = Usuario.objects.get(id=1)

        Accidente.objects.get_or_create(
            fecha=fecha,
            ubicacion=ubicacion,
            condicion_victima=condicion_victima,
            gravedad_victima=gravedad_victima,
            tipo_accidente=tipo_accidente,
            sexo_victima=sexo_victima if not pd.isna(sexo_victima) else None,
            edad_victima=edad_victima if not pd.isna(edad_victima) else None,
            cantidad_victima=cant_victima if not pd.isna(cant_victima) else None,
            usuario=usuario
        )

        print(index)