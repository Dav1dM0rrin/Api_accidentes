from autenticacion.models import Usuario
from django.contrib import admin


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido')


admin.site.register(Usuario, UsuarioAdmin)