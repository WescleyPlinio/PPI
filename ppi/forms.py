from django import forms
from .models import Projeto, Aluno, Orientador
from crispy_forms.layout import Layout, Field, Submit, Row, Column
from crispy_forms.helper import FormHelper


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ["titulo", "resumo", "objetivo", "capa", "pdf", "curso", "alunos", "orientadores", "palavras_chave", "imagens"]
        widgets = {
            "resumo": forms.Textarea(attrs={"rows": 4}),
            "objetivo": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column("titulo", css_class="form-group col-md-6 mb-3"),
                Column("capa", css_class="form-group col-md-6 mb-3"),
            ),
            Row(
                Column("resumo", css_class="form-group col-md-6 mb-3"),
                Column("imagens", css_class="form-group col-md-6 mb-3"),
            ),
            Row(
                Column("objetivo", css_class="form-group col-md-6 mb-3"),
                Column("alunos", css_class="form-group col-md-6 mb-3"),
            ),
            Row(
                Column("orientadores", css_class="form-group col-md-6 mb-3"),
                Column("curso", css_class="form-group col-md-6 mb-3"),
            ),
            "arquivo_pdf",
            "palavras_chave",
            Submit("submit", "Adicionar", css_class="btn btn-primary"),
        ) 
    
