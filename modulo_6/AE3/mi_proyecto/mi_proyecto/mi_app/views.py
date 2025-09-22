from django.shortcuts import render
from .models import Producto
from django.http import HttpResponse

def pagina_estatica(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def numeros_view(request):
    # Usamos while para generar una lista de números pares hasta 10
    numeros = []
    i = 0
    while i <= 10:
        numeros.append(i)
        i += 2  # Incrementa de 2 en 2

    # Pasamos la lista al template
    return render(request, 'numeros.html', {'numeros': numeros})