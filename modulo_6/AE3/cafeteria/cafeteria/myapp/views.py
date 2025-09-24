from django.shortcuts import render
from .models import MenuItem, Barista, Cafe, Resena, Proveedor

def index(request):
    resenas_destacadas = Resena.objects.all().order_by('-calificacion')[:3]
    return render(request, 'index.html', {'resenas_destacadas': resenas_destacadas})

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def baristas(request):
    baristas = Barista.objects.all()
    return render(request, 'baristas.html', {'baristas': baristas})

def resenas(request):
    resenas = Resena.objects.all().order_by('-fecha_creacion')
    return render(request, 'resenas.html', {'resenas': resenas})

def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})