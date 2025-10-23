""" # clientes/admin.py
from django.contrib import admin
from ordenes.models import Orden
from .models import Cliente, PerfilCliente

class PerfilInline(admin.StackedInline):
    model = PerfilCliente
    can_delete = False
    verbose_name_plural = 'Perfil'

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'created_at')
    inlines = (PerfilInline,)

@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'telefono', 'direccion')

class OrdenInline(admin.TabularInline):
    model = Orden
    extra = 1
    readonly_fields = ('fecha',)
    show_change_link = True

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')
    inlines = [OrdenInline] """
    
from django.contrib import admin
from .models import Cliente, PerfilCliente
from ordenes.models import Orden
class PerfilInline(admin.StackedInline):
    model = PerfilCliente
    can_delete = False
    verbose_name_plural = 'Perfil'
@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'telefono', 'direccion')
class OrdenInline(admin.TabularInline):
    model = Orden
    extra = 1
    readonly_fields = ('fecha',)
    show_change_link = True
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')
    inlines = [OrdenInline, PerfilInline]
@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente__nombre',)