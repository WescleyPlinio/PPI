from django import forms
from .models import Projeto, Aluno, Orientador
from .models import Comentario

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = "__all__"
        widgets = {
            "resumo": forms.Textarea(),
            "objetivo": forms.Textarea(),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto'] 
        widgets = {
            "resumo": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "objetivo": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "curso": forms.Select(attrs={"class": "form-select"}),
            "aluno": forms.Select(attrs={"class": "form-select"}),
        }
    
