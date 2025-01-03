from django.contrib import admin
from .models import Aluno, Orientador, Curso, Projeto, FotoProjeto

admin.site.register(Aluno)
admin.site.register(Orientador)
admin.site.register(Curso)
admin.site.register(Projeto)
admin.site.register(FotoProjeto)