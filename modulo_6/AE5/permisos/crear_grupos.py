import os
import sys
import django

# Configurar Django
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_root, 'permisos'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'permisos.settings')
django.setup()

from django.contrib.auth.models import Group, Permission

def crear_grupos():
    """Crear grupos con permisos específicos"""
    
    print("=== CREANDO GRUPOS DE USUARIOS ===")
    
    grupos = {
        'vendedores': ['view_ventas'],
        'compradores': ['view_compras'],
        'inventarios': ['view_inventarios'],
        'administradores': ['view_ventas', 'view_compras', 'view_inventarios']
    }
    
    for nombre_grupo, permisos in grupos.items():
        grupo, creado = Group.objects.get_or_create(name=nombre_grupo)
        if creado:
            print(f"✓ Grupo '{nombre_grupo}' creado")
            
            # Asignar permisos al grupo
            for codigo_permiso in permisos:
                try:
                    permiso = Permission.objects.get(codename=codigo_permiso)
                    grupo.permissions.add(permiso)
                    print(f"  - Permiso '{codigo_permiso}' asignado")
                except Permission.DoesNotExist:
                    print(f"  ✗ Permiso '{codigo_permiso}' no encontrado")
        else:
            print(f"✓ Grupo '{nombre_grupo}' ya existe")
    
    print("\n=== GRUPOS DISPONIBLES PARA REGISTRO ===")
    grupos_existentes = Group.objects.all()
    for grupo in grupos_existentes:
        permisos = [perm.codename for perm in grupo.permissions.all()]
        print(f"- {grupo.name}: {', '.join(permisos)}")

if __name__ == "__main__":
    crear_grupos()
