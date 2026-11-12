from django import forms
from .models import Prenda


class PrendaForm(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = ["categoria", "nombre", "descripcion", "precio", "talla", "stock"]
        widgets = {
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "talla": forms.Select(attrs={"class": "form-select"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
        }