from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CadastroForm, ProfileForm
from .models import Profile
from ppi.models import Projeto

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)

            usuario.save()

            if usuario.vinculo:
                if usuario.vinculo_id == 1:
                    grupo_nome = "Alunos"
                     
                if usuario.vinculo_id == 2: 
                    grupo_nome = "Professores"
                
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
    post = Projeto.objects.all()
    
    context = {
        "projetos" : post,
        "range" : range(2),
        "profile": profile,
    }

    return render (request, "verperfil.html", context)

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
