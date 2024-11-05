from django.contrib import admin
from accidente.models import *


# Register your models here.
class ZonaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class BarrioAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class TipoViaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class ViaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class UbicacionAdmin(admin.ModelAdmin):
    search_fields = Ubicacion.SearchableFields
    readonly_fields = ("created", "updated")


class CondicionVictimaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class GravedadVictimaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class TipoAccidenteAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class AccidenteAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Zona, ZonaAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(TipoVia, TipoViaAdmin)
admin.site.register(Via, ViaAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(CondicionVictima, CondicionVictimaAdmin)
admin.site.register(GravedadVictima, GravedadVictimaAdmin)
admin.site.register(TipoAccidente, TipoAccidenteAdmin)
admin.site.register(Accidente, AccidenteAdmin)