from django import forms
from .models import Diseño

class DiseñoForm(forms.ModelForm):
    class Meta:
        model = Diseño
        fields = ['diseñador', 'diseño', 'descripcion', 'imagen']
