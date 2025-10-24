from django.contrib import admin
from .models import Orden, DetalleOrden

class DetalleInline(admin.TabularInline):
    model = DetalleOrden
    extra = 1

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total', 'estado')
    inlines = (DetalleInline,)