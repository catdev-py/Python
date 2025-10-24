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

def agregar_al_carrito(request, bicicleta_id):
    try:
        bicicleta = Bicicleta.objects.get(id=bicicleta_id, disponible=True)
        carrito = request.session.get('carrito', {})
        carrito[str(bicicleta_id)] = carrito.get(str(bicicleta_id), 0) + 1
        request.session['carrito'] = carrito
        request.session.modified = True
        messages.success(request, f"¡{bicicleta.marca} {bicicleta.modelo} agregada al carrito!")
    except Bicicleta.DoesNotExist:
        messages.error(request, "La bicicleta no está disponible o no existe.")
    
    return redirect('lista_bicicletas')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    bicicletas_en_carrito = []
    total = 0
    
    for bicicleta_id, cantidad in carrito.items():
        try:
            bicicleta = Bicicleta.objects.get(id=int(bicicleta_id))
            subtotal = bicicleta.precio * cantidad
            total += subtotal
            bicicletas_en_carrito.append({
                'bicicleta': bicicleta,
                'cantidad': cantidad,
                'subtotal': subtotal
            })
        except (Bicicleta.DoesNotExist, ValueError):
            continue
    
    return render(request, 'bicicletas/carrito.html', {
        'bicicletas_en_carrito': bicicletas_en_carrito,
        'total': total
    })

def eliminar_del_carrito(request, bicicleta_id):
    carrito = request.session.get('carrito', {})
    bicicleta_id_str = str(bicicleta_id)
    
    if bicicleta_id_str in carrito:
        try:
            bicicleta = Bicicleta.objects.get(id=bicicleta_id)
            del carrito[bicicleta_id_str]
            request.session['carrito'] = carrito
            request.session.modified = True
            messages.success(request, f"¡{bicicleta.marca} {bicicleta.modelo} eliminada del carrito!")
        except Bicicleta.DoesNotExist:
            messages.error(request, "La bicicleta no existe.")
    
    return redirect('ver_carrito')

def actualizar_cantidad_carrito(request, bicicleta_id):
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        carrito = request.session.get('carrito', {})
        bicicleta_id_str = str(bicicleta_id)
        
        if cantidad > 0:
            carrito[bicicleta_id_str] = cantidad
        else:
            if bicicleta_id_str in carrito:
                del carrito[bicicleta_id_str]
        
        request.session['carrito'] = carrito
        request.session.modified = True
        messages.success(request, "Cantidad actualizada correctamente.")
    
    return redirect('ver_carrito')
