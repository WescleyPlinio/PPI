from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetoForm, ComentarioForm, FotoProjetoForm
from django.http import JsonResponse
from .models import Projeto, Curso, Comentario, FotoProjeto
from users.models import Profile
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.contrib import messages
from django.templatetags.static import static

def index(request):
    projetos = Projeto.objects.all().order_by('?')
    context = {
        "projetos": projetos,
    }
    return render(request, "index.html", context)

def info(request, id):
    curso = get_object_or_404(Curso, id = id)
    projetos_all = Projeto.objects.filter( curso = id )
    paginator = Paginator(projetos_all, 4)
    numero_pagina = request.GET.get('pagina')
    projetos = paginator.get_page(numero_pagina)
    context = {
        "curso" : curso,
        "projetos" : projetos,
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
    componentes = list(Profile.objects.all().values('id', 'user__email'))    
    projeto = get_object_or_404(Projeto, pk=pk) if pk else None

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)

        if form.is_valid():
            projeto = form.save()

            orientadores_ids = request.POST.getlist('orientadores')
            orientados_ids = request.POST.getlist('orientados')

            projeto.orientadores.set(orientadores_ids)
            projeto.orientados.set(orientados_ids)

            imagens = request.FILES.getlist('imagens')
            for imagem in imagens:
                FotoProjeto.objects.create(projeto=projeto, photo=imagem)

            messages.success(request, 'Projeto salvo com sucesso!')

            return redirect("post", projeto.pk)

    else:
        form = ProjetoForm(instance=projeto)

    context = {
        "form": form,
        "componentes": componentes,
        "projeto": projeto,
    }

    return render(request, "formprojeto.html", context)

@login_required
def criar_comentario(request,projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    if not hasattr(request.user, 'profile'):
        raise Http404("Perfil de usuário não encontrado.")
    
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False) 
            comentario.usuario = request.user.profile
            comentario.projeto = projeto
            comentario.save()

            messages.success(request, 'Comentário salvo com sucesso!')
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
        return JsonResponse({"sucesso": True})
    
    return JsonResponse({"erro": "Método de requisição inválido"}, status=400)

def projetos(request):
    projetos = Projeto.objects.all()

    return render(request, 'pesquisar.html', {'projetos':projetos})   


def pesquisar(request):
    query = request.GET.get('q','')
    
    resultados_titulo = Projeto.objects.filter(titulo__icontains=query)
    resultados_objetivo = Projeto.objects.filter(objetivo__icontains=query)
    resultados_resumo = Projeto.objects.filter(resumo__icontains=query)

    resultados = resultados_titulo | resultados_resumo | resultados_objetivo
    paginator = Paginator(resultados, 3)
    numero_da_pagina = request.GET.get('pagina')
    resultados_paginados = paginator.get_page(numero_da_pagina)

    projetos_novos = Projeto.objects.all().order_by("criado_em")[:6]

    context = {
        'projetos' : resultados_paginados,
        'projetos_novos' : projetos_novos,
        'query' : query,
        
    }
    return render(request, 'pesquisar.html', context)

def sobre(request):
    membros = [
        {"nome": "Ellainy Nayara", "vinculo": "Aluna", "foto":static('imgs/ellainy.png')},
        {"nome": "João Henrique", "vinculo": "Aluno", "foto":static('imgs/Joao.png')},
        {"nome": "Wescley Plínio", "vinculo": "Aluno", "foto":static('imgs/Wescley.png')},
        {"nome": "Fernanda Lígia", "vinculo": "Orientadora", "foto":static('imgs/fernanda.jpg')},
        {"nome": "Pedrina Brasil", "vinculo": "Orientadora", "foto":static('imgs/pedrinha.jpeg')},
    ]

    grupos = [membros[i:i+3] for i in range(0, len(membros), 3)]

    context = {"equipe": grupos}
    
    return render(request, "about.html", context)
