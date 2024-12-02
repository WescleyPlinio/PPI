from .models import Curso

def cursos(request):
    return {
        "cursos" : Curso.objects.all,
    }
