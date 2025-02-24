from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from .models import Projeto, Comentario, FotoProjeto, Profile

class ProjetoForm(forms.ModelForm):
    componentes = forms.ModelMultipleChoiceField(
        queryset=Profile.objects.all(),
        widget=ModelSelect2MultipleWidget(
            model=Profile,
            search_fields=['user__username__icontains', 'user__first_name__icontains', 'user__last_name__icontains']
        )
    )

    class Meta:
        model = Projeto
        fields = ['titulo', 'resumo', 'objetivo', 'componentes', 'capa', 'pdf', 'palavras_chave', 'curso']

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