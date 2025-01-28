from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm, ProfileForm
from .models import Profile
from ppi.models import Projeto

def cadastro(request):
    context = {}
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration/cadastro.html', {'form': form})
    else:
        context = {
            'form': form,
        }
    return render(request, 'registration/cadastro.html', context)

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
