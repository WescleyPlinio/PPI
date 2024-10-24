from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        "posts" : Post.objects.all,
        "range" : range(3)
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
    context = {
        "range" : range(16)
    }
    return render(request, "cursoedific.html", context)

def mamb(request):
    context = {
        "range" : range(16)
    }
    return render(request, "cursomamb.html", context)

def post(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post" : post,
    }
    return render(request, "post.html", context)