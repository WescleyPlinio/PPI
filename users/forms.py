from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import BaseUserCreationForm
from .models import User, Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class CadastroForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'curso', 'vinculo', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='col-md-6'),
                Column('email', css_class='col-md-6'),
                Column('curso', css_class='col-md-6'),
                Column('vinculo', css_class='col-md-6'),
                Column('password1', css_class='col-md-6'),
                Column('password2', css_class='col-md-6'),
                Submit('submit', 'Cadastrar', css_class='col-md-12 btn btn-dark fundo-roxinho text-uppercase'),
            )
        )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'primeiro_nome', 'ultimo_sobrenome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('primeiro_nome', css_class='col-md-6'),
                Column('ultimo_sobrenome', css_class='col-md-6'),
                Column('avatar', css_class='col-md-12'),
                Submit('submit', 'Atualizar', css_class='col-md-12 btn btn-dark fundo-roxinho'),
            )
        )