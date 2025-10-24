from django.urls import path
from . import views

app_name = 'bicicletas'

urlpatterns = [
    path('', views.lista_bicicletas, name='lista_bicicletas'),
    path('crear/', views.crear_bicicleta, name='crear_bicicleta'),
    path('actualizar/<int:pk>/', views.actualizar_bicicleta, name='actualizar_bicicleta'),
    path('eliminar/<int:pk>/', views.eliminar_bicicleta, name='eliminar_bicicleta'),
]