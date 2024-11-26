from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        "posts" : Post.objects.all,
    }
    return render(request, "index.html", context)

def login(request):
    return render(request, "login.html")

def info(request):
    post = Post.objects.all
    context = {
        "post" : post,
        "range" : range(16)
    }
    return render(request, "cursoinfo.html", context)

def edific(request):
    post = Post.objects.all
    context = {
        "post" : post,
        "range" : range(16)
    }
    return render(request, "cursoedific.html", context)

def mamb(request):
    post = Post.objects.all
    context = {
        "post" : post,
        "range" : range(16)
    }
    return render(request, "cursomamb.html", context)

def post(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post" : post,
    }
    return render(request, "post.html", context)

def addpost(request):

    context = {

    }

    if request.method == "POST":
        post = Post(titulo = request.POST['titulo'],
                    justificativa = request.POST['justificativa'],
                    capa = request.POST['capa'],
                    pdf = request.POST['pdf'],
                    resumo = request.POST['resumo'],
                    curso = request.POST['curso'],
                    alunos = request.POST['alunos'],
                    orientadores = request.POST['orientadores'],
                    )
        
        post.save()
        
        return render (request, "addpost.html", context)

    else:
        return render (request, "addpost.html", context)
    

def verperfil(request):

    post = Post.objects.all
    context = {
        "projetos" : post,
        "range" : range(3)
    }

    return render (request, "verperfil.html", context)