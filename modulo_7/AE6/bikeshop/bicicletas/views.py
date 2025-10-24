from django.shortcuts import render, redirect, get_object_or_404
from .models import Bicicleta
from .forms import BicicletaForm

def crear_bicicleta(request):
    if request.method == 'POST':
        form = BicicletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:lista_bicicletas')
    else:
        form = BicicletaForm()
    return render(request, 'bicicletas/crear_bicicleta.html', {'form': form})

def lista_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'bicicletas/lista_bicicletas.html', {'bicicletas': bicicletas})

def actualizar_bicicleta(request, pk):
    bicicleta = get_object_or_404(Bicicleta, pk=pk)
    if request.method == 'POST':
        form = BicicletaForm(request.POST, instance=bicicleta)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:lista_bicicletas')
    else:
        form = BicicletaForm(instance=bicicleta)
    return render(request, 'bicicletas/actualizar_bicicleta.html', {'form': form})

def eliminar_bicicleta(request, pk):
    bicicleta = get_object_or_404(Bicicleta, pk=pk)
    bicicleta.delete()
    return redirect('bicicletas:lista_bicicletas')