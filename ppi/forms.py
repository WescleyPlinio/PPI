from django import forms
from .models import Projeto, Aluno, Orientador
from crispy_forms.layout import Layout, Field, Submit, Row, Column
from crispy_forms.helper import FormHelper
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
    
