from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetoForm, ComentarioForm
from django.http import JsonResponse
from .models import Projeto, Curso, Comentario
from users.models import Profile
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

    componentes = list(Profile.objects.all().values('id', 'user__username'))    

    if pk:
        projeto = get_object_or_404(Projeto, pk=pk)
    else:
        projeto = None

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES,  instance=projeto)

        if form.is_valid():
            projeto = form.save()
           
            componentes_ids = request.POST.getlist('componentes')
            projeto.componentes.set(componentes_ids)

            return redirect("verperfil")
        else:
            context = {
                'form': ProjetoForm(),
            }
    else:
        form = ProjetoForm(instance=projeto)

    context = {
        "form": form,
        "componentes": componentes,
        "projeto": projeto,
    }

    return render(request, "formprojeto.html", context)

    
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

def excluir_projeto(request, pk):
    if request.method == 'POST':
        projeto = get_object_or_404(Projeto, pk=pk)
        projeto.delete()
        return JsonResponse({"Sucesso!":True})
        
    return JsonResponse({"Erro":"Método de requisição inválido"}, status = 400)

def projetos(request):
    projetos = Projeto.objects.all()

    return render(request, 'pesquisar.html', {'projetos':projetos})   


def pesquisar(request):
    posts = Projeto.objects.all()
    context = {
        "projetos" : posts,
        'pesquisas': ['Prorização e igualdade', 'Direção de hardware', 'Plantações Angiela', 'Rodeio informático', 'PPI'],
        'ideias': ['Prorização e igualdade', 'Direção de hardware', 'Plantações Angiela'],
        
    }
    return render(request, 'pesquisar.html', context)
