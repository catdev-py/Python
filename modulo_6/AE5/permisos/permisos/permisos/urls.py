from django.contrib import admin
from django.urls import path
from usuarios import views
from usuarios.views import HomeView, VentasView, ComprasView, InventariosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('ventas/', VentasView.as_view(), name='ventas'),
    path('compras/', ComprasView.as_view(), name='compras'),
    path('inventarios/', InventariosView.as_view(), name='inventarios'),
    path('logout/', views.logout_view, name='logout'),
    path('', HomeView.as_view(), name='home'),
]
