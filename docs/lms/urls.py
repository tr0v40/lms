"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name=" "),
    path('cursos/', views.cursos, name="cursos"),
    path('detalhes_da_disciplina/', views.detalhes, name="detalhes_da_disciplina"),
    path('detalhes-do-curso/', views.detalhes_curso, name="detalhes-do-curso"),
    path('formulario-curso/', views.formcur, name="formulario-curso"),
    path('formulario_discipĺina/', views.formdisc, name="formulario_discipĺina"),
    path('login/', views.login, name="login"),
    path('matricula/', views.matricula, name="matricula"),
    path('pagina_da_disciplina/', views.pag_disc, name="pagina_da_disciplina"),
    path('novo_aluno/', views.novo_aluno, name="novo_aluno"),
    path('ads/', views.ads, name="ads"),



]
