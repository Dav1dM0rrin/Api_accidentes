from autenticacion.models import Rol, Usuario
from django.contrib import admin


class RolAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido')


admin.site.register(Rol, RolAdmin)
admin.site.register(Usuario, UsuarioAdmin)