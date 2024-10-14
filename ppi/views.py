from django.shortcuts import render

def index(request):
    context = {
        "range" : range(3)
    }
    return render(request, "index.html", context)

def login(request):
    return render(request, "login.html")