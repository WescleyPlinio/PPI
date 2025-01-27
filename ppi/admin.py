from django.contrib import admin
from users.models import Profile
from .models import Aluno, Orientador, Curso, Vinculo, Projeto, FotoProjeto, Comentario

admin.site.register(Aluno)
admin.site.register(Orientador)
admin.site.register(Profile)
admin.site.register(Curso)
admin.site.register(Vinculo)
admin.site.register(Projeto)
admin.site.register(Comentario)
admin.site.register(FotoProjeto)