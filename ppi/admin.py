from django.contrib import admin
from users.models import Profile, User
from .models import Curso, Vinculo, Projeto, FotoProjeto, Comentario

admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Curso)
admin.site.register(Vinculo)
admin.site.register(Projeto)
admin.site.register(Comentario)
admin.site.register(FotoProjeto)