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
        "cursos":[
            {'nome':'Analise e Desenvolvimento de Sistemas', 'link':'/cursos/ads'},
            {'nome':'Banco de Dados', 'link':'/cursos/bd'},
            {'nome':'Gestão de Tecnologia da Informação', 'link':'/cursos/gti'},
            ],
        "resumo": ['Entender as necessidades das empresas é fundamental para fazê-las crescer e gerar bons resultados.Desta maneira, um dos caminhos para alavancar os negócios e se destacar no mercado de trabalho é o da Tecnologia.', 'O curso de Banco de Dados prepara o aluno para ser um profissional versátil e com habilidades para atuar com diversas plataformas e estruturas dedesenvolvimento e administração de sistemas de Banco de Dados, com acesso a todo o repertório técnico e teórico da área.', 'A graduação em Gestão da Tecnologia da Informação prepara você para a liderança em TI.Apto a criar soluções para problemas nas organizações, você vai fazer a administração de infraestrutura física e lógica de ambientes informatizados.'],
    }
    return render(request, 'cursos.html', context)

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

def bd(request):
    context = {
        "titulo": "Disciplina",
        "paragafo1": [""]
    }
    return render(request, 'pagina_da_disciplina.html')

def ads(request):
    context = {
        "titulo": "Disciplina",
        "paragafo1": ["Minha caceta"]
    }
    return render(request, 'ads.html')
