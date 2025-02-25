from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import Group
from .forms import CadastroForm, ProfileForm, CursoForm, VinculoForm
from .models import Profile, Curso, Vinculo, User
from ppi.models import Projeto
from django.db.models import Q

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)

            usuario.save()

            if usuario.vinculo:
                if usuario.vinculo.vinculo == "Aluno":
                    grupo_nome = "Alunos"
                     
                elif usuario.vinculo.vinculo == "Professor": 
                    grupo_nome = "Professores"
                
                elif usuario.vinculo.vinculo != "Aluno" and usuario.vinculo.vinculo != "Professor":
                    grupo_nome = "Outros"

                if grupo_nome:
                    grupo, _ = Group.objects.get_or_create(name=grupo_nome)
                    usuario.groups.add(grupo)

            return redirect('login')
        else:
            return render(request, 'registration/cadastro.html', {'form': form})

    else:
        form = CadastroForm()
        return render(request, 'registration/cadastro.html', {'form': form})

@login_required
def verperfil(request):
    profile = get_object_or_404(Profile, user=request.user)

    projetos = Projeto.objects.filter(
        Q(orientados=profile) | Q(orientadores=profile)
    ).distinct()  

    context = {
        "profile": profile,
        "projetos": projetos,
    }

    return render(request, "verperfil.html", context)

@login_required
def editarperfil(request):
    profile = request.user.profile
    context = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('verperfil')
        else:
            return render(request, 'editarperfil.html', {'form': form})
    else:
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
        }

    return render(request, "editarperfil.html", context)

def superuser_required(user):
    return user.is_superuser

@login_required
@user_passes_test(superuser_required)
def paineladmin(request):
    cursos = Curso.objects.all()
    vinculos = Vinculo.objects.all()
    usuarios = User.objects.all()
    context = {
        "cursos": cursos,
        "vinculos": vinculos,
        "usuarios": usuarios,
    }
    return render(request, 'paineladmin.html', context)

@login_required
@permission_required('users.add_curso', raise_exception=True)
def adicionarcurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('painel')
        else:
            return render(request, 'adicionarcurso.html', {'form': form})

    else:
        form = CursoForm()
        return render(request, 'adicionarcurso.html', {'form': form})
    
@login_required
@permission_required('users.change_curso', raise_exception=True)
def editarcurso(request, id_curso):
    curso = get_object_or_404(Curso, pk=id_curso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'adicionarcurso.html', {'form': form})

@login_required
@permission_required('users.delete_curso', raise_exception=True)
def removercurso(request, id_curso):
    curso = get_object_or_404(Curso, pk=id_curso)
    
    if request.method == 'POST':
        curso.delete()
        return redirect('painel')  

    return redirect('index')  


@login_required
@permission_required('users.add_vinculo', raise_exception=True)
def adicionarvinculo(request):
    if request.method == 'POST':
        form = VinculoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('painel')
        else:
            return render(request, 'adicionarvinculo.html', {'form': form})

    else:
        form = VinculoForm()
        return render(request, 'adicionarvinculo.html', {'form': form})
    
@login_required
@permission_required('users.change_vinculo', raise_exception=True)
def editarvinculo(request, id_vinculo):
    vinculo = get_object_or_404(Vinculo, pk=id_vinculo)
    if request.method == 'POST':
        form = VinculoForm(request.POST, instance=vinculo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VinculoForm(instance=vinculo)
    return render(request, 'adicionarvinculo.html', {'form': form})

@login_required
@permission_required('users.delete_vinculo', raise_exception=True)
def removervinculo(request, id_vinculo):
    vinculo = get_object_or_404(Vinculo, pk=id_vinculo)
    
    if request.method == 'POST':
        vinculo.delete()
        return redirect('painel')  

    return redirect('index')  