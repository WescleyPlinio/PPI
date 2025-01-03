from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from .models import Projeto, Aluno, Orientador

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
    
    widgets = {
        'usuarios1': ModelSelect2MultipleWidget(
            model=Aluno,
            search_fields=['nome__icontains', 'email__icontains'],  # Pesquisar pelo nome ou email
        ),
        'usuarios2': ModelSelect2MultipleWidget(
            model=Orientador,
            search_fields=['nome__icontains', 'email__icontains'],  # Pesquisar pelo nome ou email
         ),
    }
