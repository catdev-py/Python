from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('ventas/', views.view_ventas, name='ventas'),
    path('compras/', views.view_compras, name='compras'),
    path('inventarios/', views.view_inventarios, name='inventarios'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
]
