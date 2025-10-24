from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ordenes, name='lista_ordenes'),
    path('crear/', views.crear_orden, name='crear_orden'),
    path('<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
    path('vaciar-carrito/', views.vaciar_carrito, name='vaciar_carrito'),
]
