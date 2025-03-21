from django.contrib import admin
from autenticacion.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido')

    def save_model(self, request, obj, form, change):
        if not change or "password" in form.changed_data:  # Si es nuevo o se cambió la contraseña
            obj.set_password(obj.password)  # Encripta la contraseña antes de guardarla
        super().save_model(request, obj, form, change)

admin.site.register(Usuario, UsuarioAdmin)
