from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import transaction, IntegrityError
from django.contrib import messages
from .models import Bicicleta
from .forms import BicicletaForm

def lista_bicicletas(request):
    bicicletas = Bicicleta.objects.all().order_by('-id')
    return render(request, 'bicicletas/lista_bicicletas.html', {'bicicletas': bicicletas})

def detalle_bicicleta(request, pk):
    bici = get_object_or_404(Bicicleta, pk=pk)
    return render(request, 'bicicletas/detalle_bicicleta.html', {'bicicleta': bici})

def crear_bicicleta(request):
    if request.method == 'POST':
        form = BicicletaForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    bici = form.save()
                messages.success(request, "Bicicleta creada correctamente.")
                return redirect('lista_bicicletas')
            except IntegrityError:
                messages.error(request, "Ocurrió un error al crear la bicicleta.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = BicicletaForm()
    return render(request, 'bicicletas/bicicleta_form.html', {'form': form, 'accion': 'Crear'})

def actualizar_bicicleta(request, pk):
    bici = get_object_or_404(Bicicleta, pk=pk)
    if request.method == 'POST':
        form = BicicletaForm(request.POST, instance=bici)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                messages.success(request, "Bicicleta actualizada correctamente.")
                return redirect('lista_bicicletas')
            except IntegrityError:
                messages.error(request, "Ocurrió un error al actualizar la bicicleta.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = BicicletaForm(instance=bici)
    return render(request, 'bicicletas/bicicleta_form.html', {'form': form, 'accion': 'Actualizar'})

def confirmar_eliminar_bicicleta(request, pk):
    bici = get_object_or_404(Bicicleta, pk=pk)
    if request.method == 'POST':
        bici.delete()
        messages.success(request, "Bicicleta eliminada.")
        return redirect('lista_bicicletas')
    return render(request, 'bicicletas/bicicleta_confirm_delete.html', {'bicicleta': bici})
