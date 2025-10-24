from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_bicicletas, name='lista_bicicletas'),
    path('crear/', views.crear_bicicleta, name='crear_bicicleta'),
    path('<int:pk>/', views.detalle_bicicleta, name='detalle_bicicleta'),
    path('actualizar/<int:pk>/', views.actualizar_bicicleta, name='actualizar_bicicleta'),
    path('eliminar/<int:pk>/', views.confirmar_eliminar_bicicleta, name='confirmar_eliminar_bicicleta'),
]