from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from .models import Orden, DetalleOrden
from bicicletas.models import Bicicleta
from clientes.models import Cliente

def crear_orden(request):
    carrito = request.session.get('carrito', {})
    
    if not carrito:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('ver_carrito')
    
    # Para este ejemplo, usaremos un cliente por defecto
    # En una aplicación real, esto vendría del usuario autenticado
    try:
        cliente = Cliente.objects.first()
        if not cliente:
            messages.error(request, "No hay clientes registrados en el sistema.")
            return redirect('ver_carrito')
    except Cliente.DoesNotExist:
        messages.error(request, "No hay clientes registrados en el sistema.")
        return redirect('ver_carrito')
    
    try:
        with transaction.atomic():
            # Crear la orden
            orden = Orden.objects.create(
                cliente=cliente,
                total=0  # Se calculará después
            )
            
            total_orden = 0
            
            # Crear los detalles de la orden
            for bicicleta_id, cantidad in carrito.items():
                try:
                    bicicleta = Bicicleta.objects.get(id=int(bicicleta_id))
                    subtotal = bicicleta.precio * cantidad
                    total_orden += subtotal
                    
                    DetalleOrden.objects.create(
                        orden=orden,
                        bicicleta=bicicleta,
                        cantidad=cantidad,
                        precio_unitario=bicicleta.precio
                    )
                    
                except (Bicicleta.DoesNotExist, ValueError):
                    continue
            
            # Actualizar el total de la orden
            orden.total = total_orden
            orden.save()
            
            # Limpiar el carrito
            request.session['carrito'] = {}
            request.session.modified = True
            
            messages.success(request, f"¡Orden #{orden.id} creada exitosamente! Total: ${total_orden}")
            
    except Exception as e:
        messages.error(request, f"Error al crear la orden: {str(e)}")
        return redirect('ver_carrito')
    
    return redirect('detalle_orden', orden_id=orden.id)

def detalle_orden(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id)
    detalles = orden.detalleorden_set.all()
    
    # Calcular subtotales para cada detalle
    detalles_con_subtotal = []
    for detalle in detalles:
        detalles_con_subtotal.append({
            'bicicleta': detalle.bicicleta,
            'cantidad': detalle.cantidad,
            'precio_unitario': detalle.precio_unitario,
            'subtotal': detalle.cantidad * detalle.precio_unitario
        })
    
    return render(request, 'ordenes/detalle_orden.html', {
        'orden': orden,
        'detalles': detalles_con_subtotal
    })

def lista_ordenes(request):
    ordenes = Orden.objects.all().order_by('-fecha')
    return render(request, 'ordenes/lista_ordenes.html', {'ordenes': ordenes})

def vaciar_carrito(request):
    request.session['carrito'] = {}
    request.session.modified = True
    messages.success(request, "Carrito vaciado correctamente.")
    return redirect('ver_carrito')
