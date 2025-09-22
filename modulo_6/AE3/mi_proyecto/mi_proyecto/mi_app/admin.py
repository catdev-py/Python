from django.contrib import admin
from .models import Producto  # Importa tu modelo

# Configuración básica del admin
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'descripcion')  # Columnas que se mostrarán en la lista
    list_display_links = ('nombre',)  # Qué campo es clickeable para editar
    search_fields = ('nombre', 'descripcion')  # Campos para buscar
    list_filter = ('precio',)  # Filtros laterales
    ordering = ('id',)  # Orden por defecto
