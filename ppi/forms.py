from django import forms
from .models import Projeto, Comentario

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = "__all__"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto'] 
        widgets = {
            "resumo": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "objetivo": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "curso": forms.Select(attrs={"class": "form-select"}),
            "componentes": forms.Select(attrs={"class": "form-select"}),
        }
    
