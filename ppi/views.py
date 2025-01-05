from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetoForm
from django.http import JsonResponse
from .models import Projeto, Curso, Aluno, Orientador
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
    posts = Projeto.objects.filter( curso = id )
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
            projeto = form.save()
           
            alunos_ids = request.POST.getlist('alunos') 
            orientadores_ids = request.POST.getlist('orientadores')
            projeto.alunos.set(alunos_ids)
            projeto.orientadores.set(orientadores_ids)

            return redirect("pesquisar") 
    else:
        form = ProjetoForm()

    alunos = Aluno.objects.all()
    orientadores = Orientador.objects.all()

    return render(request, "addpost.html", {
        "form": form,
        "alunos": alunos,
        "orientadores": orientadores,
    })

def aluno_search(request):
    query = request.GET.get('q', '')
    alunos = Aluno.objects.filter(nome__icontains=query, tipo='aluno')[:10]
    results = [{'id': aluno.id, 'text': f"{aluno.nome} ({aluno.email})"} for aluno in alunos]
    return JsonResponse({'results': results})

def professor_search(request):
    query = request.GET.get('q', '')
    orientadores = Orientador.objects.filter(nome__icontains=query, tipo='professor')[:10]
    results = [{'id': orientador.id, 'text': f"{orientador.nome} ({orientador.email})"} for orientador in orientadores]
    return JsonResponse({'results': results})

    
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
