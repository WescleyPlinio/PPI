from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        widgets = {
            'usuarios1': forms.CheckboxSelectMultiple(),  # Professores
            'usuarios2': forms.CheckboxSelectMultiple(),  # Alunos
        }