from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin personalizado para el modelo CustomUser"""
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    
    # Usar fieldsets del UserAdmin sin agregar campos duplicados
    # Los campos 'groups' y 'user_permissions' ya están incluidos en UserAdmin.fieldsets
