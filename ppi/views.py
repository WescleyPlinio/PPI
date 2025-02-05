from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetoForm, ComentarioForm, FotoProjetoForm
from django.http import JsonResponse
from .models import Projeto, Curso, Comentario, FotoProjeto
from users.models import Profile
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404

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
            comentario.usuario = request.user.profile
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
@permission_required('ppi.add_projeto', raise_exception=True)
def formprojeto(request, pk=None):
    componentes = list(Profile.objects.all().values('id', 'user__username'))    
    projeto = get_object_or_404(Projeto, pk=pk) if pk else None

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)

        if form.is_valid():
            projeto = form.save()

            componentes_ids = request.POST.getlist('componentes')
            projeto.componentes.set(componentes_ids)

            imagens = request.FILES.getlist('imagens')
            for imagem in imagens:
                FotoProjeto.objects.create(projeto=projeto, photo=imagem)

            return redirect("verperfil")

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

    # Verifica se o usuário tem um perfil associado
    if not hasattr(request.user, 'profile'):
        raise Http404("Perfil de usuário não encontrado.")
    
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False) 
            comentario.usuario = request.user.profile
            comentario.projeto = projeto
            comentario.save() 
            return redirect('post')
    else:
        form = ComentarioForm()

    return render(request, 'criar_comentario.html', { 'form': form, 'projeto': projeto })


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
