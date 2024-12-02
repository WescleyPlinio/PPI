from django.shortcuts import render, get_object_or_404
from .models import Projeto, Curso

def index(request):
    context = {
        "posts" : Projeto.objects.all,
    }
    return render(request, "index.html", context)

def login(request):
    return render(request, "login.html")

def info(request, id):
    curso = get_object_or_404(Curso, id = id)
    post = Projeto.objects.all
    context = {
        "curso" : curso,
        "post" : post,
        "range" : range(4)
    }
    return render(request, "cursofeed.html", context)

def post(request, id):
    post = Projeto.objects.get(id=id)
    context = {
        "post" : post,
    }
    return render(request, "post.html", context)

def addpost(request):

    context = {

    }

    if request.method == "POST":
        post = Projeto(titulo = request.POST['titulo'],
                    descricao = request.POST['descricao'],
                    capa = request.POST['capa'],
                    pdf = request.POST['pdf'],
                    resumo = request.POST['resumo'],
                    curso = request.POST['curso'],
                    usuarios1 = request.POST['usuarios1'],
                    usuarios2 = request.POST['usuarios2'],
                    )
        
        post.save()
        
        return render (request, "addpost.html", context)

    else:
        return render (request, "addpost.html", context)
    

def verperfil(request):

    post = Projeto.objects.all
    context = {
        "projetos" : post,
        "range" : range(3)
    }

    return render (request, "verperfil.html", context)

def editarperfil(request):

    context = {
        
    }

    return render(request, "editarperfil.html", context)