from django.shortcuts import render

def index(request):
    context = {
        "range" : range(6)
    }
    return render(request, "index.html", context)

def login(request):
    return render(request, "login.html")

def info(request):
    context = {
        "range" : range(16)
    }
    return render(request, "cursoinfo.html", context)