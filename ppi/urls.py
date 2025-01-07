from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("login/", views.login, name = "login"),
    path("cadastro/", views.cadastro, name = "cadastro"),
    path("projetos/<int:id>/", views.info, name = "projetos"),
    path("post/<int:id>/", views.post, name = "post"),
    path("perfil/", views.verperfil, name = "verperfil"),
    path("editar_perfil/", views.editarperfil, name = "editarperfil"),
    path("pesquisar/", views.pesquisar, name = "pesquisar"),
    path('search/alunos/', views.aluno_search, name='aluno-search'),
    path('search/professores/', views.professor_search, name='professor-search'),
    path("form_projeto/", views.formprojeto, name = "form_post"),
    path('projeto/<int:pk>/', views.formprojeto, name='editar_projeto'), 
    path('projeto/excluir/<int:pk>/', views.excluir_projeto, name='excluir_projeto'),
]



