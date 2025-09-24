from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('baristas/', views.baristas, name='baristas'),
    path('menu/', views.menu, name='menu'),
    path('resenas/', views.resenas, name='resenas'),
    path('proveedores/', views.proveedores, name='proveedores'),
]
