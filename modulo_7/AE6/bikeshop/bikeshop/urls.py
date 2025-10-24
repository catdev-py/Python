from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('bicicletas.urls', 'bicicletas'))), 
    path('', include(('bicicletas.urls', 'bicicletas'))), 
]
