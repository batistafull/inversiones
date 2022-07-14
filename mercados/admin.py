from django.contrib import admin
from mercados.models import Persona

# Register your models here.


class PersonaAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido")
    search_fields=("nombre","apellido")
    list_filter=("nombre","apellido")

admin.site.register(Persona,PersonaAdmin)