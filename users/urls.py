from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path("perfil/", views.verperfil, name = "verperfil"),
    path("editar_perfil/", views.editarperfil, name = "editarperfil"),
]
