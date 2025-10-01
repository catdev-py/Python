from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import logout

def register(request):
    # Creamos una clase inline que use CustomUser
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name', 'last_name')  # agrega campos si quieres

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_name = request.POST.get('group')
            if group_name:
                user.groups.add(group_name)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required

@login_required
def view_ventas(request):
    return render(request, 'ventas.html', {'title': 'Ventas'})

@login_required
def view_compras(request):
    return render(request, 'compras.html', {'title': 'Compras'})

@login_required
def view_inventarios(request):
    return render(request, 'inventarios.html', {'title': 'Inventarios'})

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')
