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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['texto'].widget.attrs.update({
            'class': 'form-control mb-2 bg-transparent border-0 rounded-0 border-bottom text-white',
            'placeholder': 'Digite seu comentário',
            'rows': '1',
            'required': 'true'
        })