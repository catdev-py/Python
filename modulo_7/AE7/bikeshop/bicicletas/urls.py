from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_bicicletas, name='lista_bicicletas'),
    path('crear/', views.crear_bicicleta, name='crear_bicicleta'),
    path('<int:pk>/', views.detalle_bicicleta, name='detalle_bicicleta'),
    path('actualizar/<int:pk>/', views.actualizar_bicicleta, name='actualizar_bicicleta'),
    path('eliminar/<int:pk>/', views.confirmar_eliminar_bicicleta, name='confirmar_eliminar_bicicleta'),
    path('agregar-carrito/<int:bicicleta_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/eliminar/<int:bicicleta_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/actualizar/<int:bicicleta_id>/', views.actualizar_cantidad_carrito, name='actualizar_cantidad_carrito'),
]
