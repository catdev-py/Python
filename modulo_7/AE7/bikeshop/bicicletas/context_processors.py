def carrito_context(request):
    """Context processor para agregar información del carrito a todos los templates"""
    carrito = request.session.get('carrito', {})
    total_items = sum(carrito.values())
    
    return {
        'carrito_total_items': total_items,
        'carrito_vacio': total_items == 0
    }
