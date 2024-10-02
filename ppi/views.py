from django.shortcuts import render

def index(request):
    context = {
        "range" : range(3)
    }
    return render(request, "index.html", context)
