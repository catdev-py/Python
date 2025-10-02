import os
import sys
import django

# Configurar Django
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_root, 'permisos'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'permisos.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from usuarios.models import CustomUser

def crear_grupos_y_permisos():
    """Crear grupos de usuarios con permisos específicos"""
    
    print("=== CREANDO GRUPOS Y PERMISOS ===")
    
    # Crear grupos
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

def crear_usuarios_ejemplo():
    """Crear usuarios de ejemplo para probar los permisos"""
    
    print("\n=== CREANDO USUARIOS DE EJEMPLO ===")
    
    usuarios = [
        {
            'username': 'vendedor1',
            'email': 'vendedor1@empresa.com',
            'password': 'test123',
            'groups': ['vendedores']
        },
        {
            'username': 'comprador1',
            'email': 'comprador1@empresa.com',
            'password': 'test123',
            'groups': ['compradores']
        },
        {
            'username': 'inventario1',
            'email': 'inventario1@empresa.com',
            'password': 'test123',
            'groups': ['inventarios']
        },
        {
            'username': 'admin1',
            'email': 'admin1@empresa.com',
            'password': 'test123',
            'groups': ['administradores']
        }
    ]
    
    for datos_usuario in usuarios:
        username = datos_usuario['username']
        
        # Verificar si el usuario ya existe
        if CustomUser.objects.filter(username=username).exists():
            print(f"✓ Usuario '{username}' ya existe")
            continue
            
        # Crear usuario
        usuario = CustomUser.objects.create_user(
            username=username,
            email=datos_usuario['email'],
            password=datos_usuario['password']
        )
        
        # Asignar grupos
        for nombre_grupo in datos_usuario['groups']:
            try:
                grupo = Group.objects.get(name=nombre_grupo)
                usuario.groups.add(grupo)
                print(f"✓ Usuario '{username}' creado y asignado al grupo '{nombre_grupo}'")
            except Group.DoesNotExist:
                print(f"✗ Grupo '{nombre_grupo}' no encontrado para usuario '{username}'")

def verificar_permisos():
    """Verificar que los permisos estén funcionando correctamente"""
    
    print("\n=== VERIFICANDO PERMISOS ===")
    
    usuarios = CustomUser.objects.all()
    
    for usuario in usuarios:
        print(f"\nUsuario: {usuario.username}")
        print(f"Grupos: {[g.name for g in usuario.groups.all()]}")
        
        permisos = {
            'view_ventas': usuario.has_perm('usuarios.view_ventas'),
            'view_compras': usuario.has_perm('usuarios.view_compras'),
            'view_inventarios': usuario.has_perm('usuarios.view_inventarios')
        }
        
        for permiso, tiene_permiso in permisos.items():
            estado = "✓" if tiene_permiso else "✗"
            print(f"  {estado} {permiso}")

if __name__ == "__main__":
    print("SCRIPT DE PRUEBA DE PERMISOS")
    print("=" * 40)
    
    try:
        crear_grupos_y_permisos()
        crear_usuarios_ejemplo()
        verificar_permisos()
        
        print("\n" + "=" * 40)
        print("✓ Configuración completada exitosamente")
        print("\nPara probar la aplicación:")
        print("1. Ejecuta: python manage.py runserver")
        print("2. Ve a http://localhost:8000")
        print("3. Inicia sesión con alguno de los usuarios creados:")
        print("   - vendedor1 / test123 (solo puede ver ventas)")
        print("   - comprador1 / test123 (solo puede ver compras)")
        print("   - inventario1 / test123 (solo puede ver inventarios)")
        print("   - admin1 / test123 (puede ver todo)")
        
    except Exception as e:
        print(f"\n✗ Error durante la configuración: {e}")
        print("Asegúrate de que las migraciones estén aplicadas:")
        print("python manage.py migrate")
