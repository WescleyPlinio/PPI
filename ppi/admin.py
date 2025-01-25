from django.contrib import admin
from .models import Aluno, Orientador, Curso, Vinculo, Projeto, FotoProjeto, Comentario

admin.site.register(Aluno)
admin.site.register(Orientador)
admin.site.register(Curso)
admin.site.register(Vinculo)
admin.site.register(Projeto)
admin.site.register(Comentario)
admin.site.register(FotoProjeto)