from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("login/", views.login, name = "login"),
    path("projetos/info/", views.info, name = "pinfo"),
    path("projetos/edific/", views.edific, name = "pedific"),
    path("projetos/mamb/", views.mamb, name = "pmamb"),
    path("post/<int:id>/", views.post, name = "post"),
    path("novos_projetos/", views.addpost, name = "form_post"),
]


