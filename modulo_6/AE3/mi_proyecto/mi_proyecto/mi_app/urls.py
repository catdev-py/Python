from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home, name='home'),  # aquí se define 'home'
    path('acerca-de/', views.about, name='about'),
    path('productos/', views.lista_productos, name='productos'),
    path('', views.pagina_estatica, name='pagina_estatica'),
    path('numeros/', views.numeros_view, name='numeros'),
]