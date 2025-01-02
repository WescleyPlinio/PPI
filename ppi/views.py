from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetoForm
from .models import Projeto, Curso
from django.core.paginator import Paginator


def index(request):
    posts = Projeto.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "index.html", context)

def login(request):
    return render(request, "login.html")

def cadastro(request):
    return render(request, "cadastro.html")

def info(request, id):
    curso = get_object_or_404(Curso, id = id)
    posts = Projeto.objects.filter( curso = curso )
    context = {
        "curso" : curso,
        "projetos" : posts,
        "range" : range(3)
    }
    return render(request, "cursofeed.html", context)

def post(request, id):
    post = Projeto.objects.get(id=id)
    context = {
        "post" : post,
    }
    return render(request, "post.html", context)

def adicionar_projetos(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            form.save()
            form.save_m2m() 
            return redirect('projetos')
    else:
        form = ProjetoForm()
    return render(request, 'addpost.html', {'form': form})

    
def projetos(request):
    projetos = Projeto.oblects.all()

    return render(request, 'pesquisar.html', {'projetos':projetos})   

def verperfil(request):

    post = Projeto.objects.all
    context = {
        "projetos" : post,
        "range" : range(2)
    }

    return render (request, "verperfil.html", context)

def editarperfil(request):

    context = {
        
    }

    return render(request, "editarperfil.html", context)


def pesquisar(request):
    posts = Projeto.objects.all()
    context = {
        "projetos" : posts,
        'pesquisas': ['Prorização e igualdade', 'Direção de hardware', 'Plantações Angiela', 'Rodeio informático', 'PPI'],
        'ideias': ['Prorização e igualdade', 'Direção de hardware', 'Plantações Angiela'],
        
    }
    return render(request, 'pesquisar.html', context)
