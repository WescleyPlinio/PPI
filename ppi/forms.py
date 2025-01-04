from django import forms
from .models import Projeto, Aluno, Orientador
from django_select2.forms import ModelSelect2MultipleWidget

class ProjetoForm(forms.ModelForm):
    alunos = forms.ModelMultipleChoiceField(
        queryset=Aluno.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        label="Alunos"
        
    )

    orientadores = forms.ModelMultipleChoiceField(
        queryset=Orientador.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        label="Orientadores"
    )

    class Meta:
        model = Projeto
        fields = ["titulo", "resumo", "objetivo", "capa", "pdf", "curso", "alunos", "orientadores", "palavras_chave", "imagens"]
