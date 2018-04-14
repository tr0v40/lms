from django.shortcuts import render
from core import views

# Create your views here.
def index(request):
    context ={
        "titulo": "Home",

    }
    return render(request, 'index.html', context)

def cursos(request):
    return render(request, 'cursos.html')

def detalhes(request):
    return render(request, 'detalhes-da-disciplina.html')

def detalhes_curso(request):
    return render(request, 'detalhes-do-curso.html')

def formcur(request):
    return render(request, 'formulario-curso.html')

def formdisc(request):
    return render(request, 'formulario_disciplina.html')

def login(request):
    return render(request, 'login.html')

def matricula(request):
    return render(request, 'matricula.html')

def novo_aluno(request):
    return render(request, 'novo_aluno.html')

def pag_disc(request):
    return render(request, 'pagina_da_disciplina.html')
