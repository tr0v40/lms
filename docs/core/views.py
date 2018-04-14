from django.shortcuts import render
from core import views

# Create your views here.
def index(request):
    context = {
        "titulo": "Home",

    }
    return render(request, 'index.html', context)


def cursos(request):
    context = {
        "titulo": "Cursos",

    }
    return render(request, 'cursos.html')

def detalhes(request):
    context = {
        "titulo": "Detalhes",

    }
    return render(request, 'detalhes-da-disciplina.html')

def detalhes_curso(request):
    context = {
        "titulo": "Detalhe do Curso",

    }
    return render(request, 'detalhes-do-curso.html')

def formcur(request):
    context = {
        "titulo": "Curso",

    }
    return render(request, 'formulario-curso.html')

def formdisc(request):
    context = {
        "titulo": "Disciplina",

    }
    return render(request, 'formulario_disciplina.html')

def login(request):
    context = {
        "titulo": "Login",

    }
    return render(request, 'login.html')

def matricula(request):
    context = {
        "titulo": "Matricula",

    }
    return render(request, 'matricula.html')

def novo_aluno(request):
    context = {
        "titulo": "Cadastro de Aluno",

    }
    return render(request, 'novo_aluno.html')

def pag_disc(request):
    context = {
        "titulo": "Disciplina",

    }
    return render(request, 'pagina_da_disciplina.html')
----------
def bd(request):
    context = {
        "titulo": "Disciplina",
        "paragafo1": ["

        "
         ]
    }
    return render(request, 'pagina_da_disciplina.html')

def ads(request):
    context = {
        "titulo": "Disciplina",
        "paragafo1": ["
        Minha caceta
        "
         ]
    }
    return render(request, 'ads.html')
