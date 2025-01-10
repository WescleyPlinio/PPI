from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetoForm, ComentarioForm
from django.http import JsonResponse
from .models import Projeto, Curso, Aluno, Orientador, Comentario
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

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
    projeto = get_object_or_404(Projeto, id=id)
    comentarios = projeto.comentarios.all() 

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.projeto = projeto
            comentario.save()
            return redirect('post', id=projeto.id)
    else:
        form = ComentarioForm()

    context = {
        'projeto': projeto,
        'comentarios': comentarios,
        'form': form
    }

    return render(request, "post.html", context)


@login_required
def formprojeto(request, pk=None):
    if pk:
        projeto = get_object_or_404(Projeto, pk=pk)
    else:
        projeto = None

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES,  instance=projeto)
        if form.is_valid():
            projeto = form.save()
           
            alunos_ids = request.POST.getlist('alunos') 
            orientadores_ids = request.POST.getlist('orientadores')
            projeto.alunos.set(alunos_ids)
            projeto.orientadores.set(orientadores_ids)

            return redirect("verperfil") 
    else:
        form = ProjetoForm(instance=projeto)

    alunos = Aluno.objects.all()
    orientadores = Orientador.objects.all()

    return render(request, "formprojeto.html", {
        "form": form,
        "alunos": alunos,
        "orientadores": orientadores,
        "projeto": projeto,
    })


def criar_comentario(request,projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False) 
            comentario.usuario = request.user 
            comentario.save() 
            print(comentario)
            return redirect('post')
    else:
        form = ComentarioForm()

    return render(request, 'criar_comentario.html', {'form': form})


def listar_comentarios(request):
    comentarios = Comentario.objects.all().order_by('-criado_em')
    return render(request, 'post.html', {'comentarios': comentarios})


@login_required
def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'GET':
        projeto.delete()
        return redirect('verperfil')
        
    return render(request, 'projeto_confirm_delete.html', {'projeto': projeto}) 


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
    projetos = Projeto.objects.all()

    return render(request, 'pesquisar.html', {'projetos':projetos})   

def verperfil(request):

    post = Projeto.objects.all()
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
