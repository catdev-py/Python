from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView
from .models import CustomUser
from .mixins import ProtectedTemplateView, PermissionProtectedTemplateView

def register(request):
    from django.contrib.auth.models import Group
    
    # Creamos una clase inline que use CustomUser
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name', 'last_name')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Asignar grupo según la selección del usuario
            group_name = request.POST.get('group')
            if group_name:
                try:
                    group = Group.objects.get(name=group_name)
                    user.groups.add(group)
                except Group.DoesNotExist:
                    # Si el grupo no existe, asignar permisos básicos
                    pass
            
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    # Obtener grupos disponibles para mostrar en el template
    groups = Group.objects.all()
    
    return render(request, 'register.html', {'form': form, 'groups': groups})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

# Vistas basadas en clases con mixins de permisos
class HomeView(TemplateView):
    """Vista para la página de inicio (pública)"""
    template_name = 'home.html'


class VentasView(PermissionProtectedTemplateView):
    """Vista protegida para ventas - requiere permiso 'view_ventas'"""
    template_name = 'ventas.html'
    permission_required = 'usuarios.view_ventas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ventas'
        return context


class ComprasView(PermissionProtectedTemplateView):
    """Vista protegida para compras - requiere permiso 'view_compras'"""
    template_name = 'compras.html'
    permission_required = 'usuarios.view_compras'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Compras'
        return context


class InventariosView(PermissionProtectedTemplateView):
    """Vista protegida para inventarios - requiere permiso 'view_inventarios'"""
    template_name = 'inventarios.html'
    permission_required = 'usuarios.view_inventarios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inventarios'
        return context

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def handler403(request, exception=None):
    """Manejador personalizado para errores 403 (Permiso denegado)"""
    return render(request, '403.html', status=403)


def handler404(request, exception=None):
    """Manejador personalizado para errores 404 (Página no encontrada)"""
    return render(request, '404.html', status=404)
