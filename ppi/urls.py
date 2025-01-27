from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("projetos/<int:id>/", views.info, name = "projetos"),
    path("post/<int:id>/", views.post, name = "post"),
    path("pesquisar/", views.pesquisar, name = "pesquisar"),
    path("form_projeto/", views.formprojeto, name = "form_post"),
    path('projeto/<int:pk>/', views.formprojeto, name='editar_projeto'), 
    path('projeto/<int:pk>/comentario', views.criar_comentario, name='comentario'), 
    path('projeto/excluir/<int:pk>/', views.excluir_projeto, name='excluir_projeto'),
]



