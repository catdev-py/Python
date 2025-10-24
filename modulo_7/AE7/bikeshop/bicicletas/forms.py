from django import forms
from .models import Bicicleta

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['marca', 'modelo', 'tipo', 'precio', 'disponible', 'anio']