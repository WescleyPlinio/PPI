from django import forms
from .models import Projeto, Comentario, FotoProjeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'resumo', 'objetivo', 'capa', 'pdf', 'palavras_chave', 'curso']

class FotoProjetoForm(forms.ModelForm):
    class Meta:
        model = FotoProjeto
        fields = ['photo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        labels = {
            'texto': ''
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['texto'].widget.attrs.update({
            'class': 'form-control mb-2 bg-light rounded',
            'rows': '1',
            'required': 'true',
            'placeholder': 'Digite seu comentário',
        })