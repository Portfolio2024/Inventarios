from django import forms
from .models import *

class Formulario_Producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "proveedor", "categoria", "cantidad", "precio"]