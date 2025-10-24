from django.contrib import admin
from .models import Bicicleta

@admin.register(Bicicleta)
class BicicletaAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'tipo', 'precio', 'disponible')
    search_fields = ('marca', 'modelo')

