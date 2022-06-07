from multiprocessing.reduction import duplicate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import *
from django.db.models import Count
from .forms import *


# CREATE - PESQUISA DE SATISFAÇÃO

def PesquisaSatisfacao(request):
    context = {}
    form = FaleConoscoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, 'faleConosco/pesquisadesatisfacao.html', context)  


# READ - GUIA MÉDICO

def viewGuiaMedico(request):
    medico = Medico.objects.order_by('Especialidade')
    especialidade = Medico.objects.values('Especialidade').distinct()
    return render(request, "guiaMedico.html", {"medico": medico, "especialidade":especialidade})

# READ - NOTICIAS

def viewNoticia(request):
    noticia = Noticia.objects.order_by('-Data')
    return render(request, "noticias.html", {"noticia": noticia})

def viewDetailNoticia(request, id):
    noticia = Noticia.objects.all()
    detailNoticia = get_object_or_404(noticia, pk=id)
    return render(request, "detailNoticias.html", {"detailNoticia":detailNoticia, "id":id})


# READ - PARCEIROS

def viewParceiros(request):
    parceiro = Parceiros.objects.all()
    return render(request, "parceiros.html", {"parceiro": parceiro})

# READ - CONVENIOS

def viewConvenio(request):
    convenio = Convenio.objects.all()
    return render(request, "convenio.html", {"convenio": convenio})

# QUEM SOMOS

# READ - DIRETORIA E HISTORIA HOSPITAL LAUREANO

def viewDiretoriaHospital(request):
    diretoria = Diretoria.objects.all()
    return render(request, "quemSomos/diretoriahospital.html", {"diretoria": diretoria})

def viewHistoriaHospital(request):
    return render(request, "quemSomos/historiaHospital.html", {})

# READ - DIRETORIA E HISTORIA FUNDAÇÃO Laureano

def viewHistoriaFundacao(request):
    return render(request, "quemSomos/historiaFundacao.html", {})

def viewDiretoriaFundacao(request):
    diretoriaexecutiva = DiretoriaExecutiva.objects.all()
    conselho = ConselhoDeliberativo.objects.all()
    return render(request, "quemSomos/diretoriaFundacao.html", {"diretoria-executiva": diretoriaexecutiva, "conselho": conselho})

# READ - GALERIA

def viewGaleria(request):
    galeria = Galeria.objects.order_by('Categoria')
    categoria = Galeria.objects.values('Categoria').distinct()
    return render(request, "quemSomos/galeria.html", {"galeria": galeria, "categoria": categoria})

# READ - PREMIOS E CERTIFICAÇÕES


# READ - TRANSPARÊNCIA

def viewTransparencia(request):
    transparencia = Transparencia.objects.all()
    return render(request, "transparencia.html", {"transparencia": transparencia})

#PATH

def viewHome(request):
    banner = Banner.objects.all()
    premio = Premio.objects.all()
    noticia = Noticia.objects.order_by('-Data')
    convenio = Convenio.objects.all()
    
    return render(request, "home.html", {"banner": banner , "noticia": noticia, "premio": premio, "convenio": convenio})


def vieweventos(request):
    return render(request, "eventos.html", {})

def viewdoacao(request):
    return render(request, "doacao.html", {})

def viewNossaMissao(request):
    return render(request, "quemSomos/nossaMissao.html")


# Path FaleConosco
def viewTrabalheConosco(request):
    return render(request, 'faleConosco/trabalheconosco.html')

def viewOuvidoria(request):
    return render(request, "faleConosco/ouvidoria.html")


def viewSejaumResidente(request):
    return render(request, 'faleConosco/sejaumresidente.html')


# Path Serviços

def viewExames(request):
    return render(request, 'servicos/exames.html')

def viewConsultas(request):
    return render(request, 'servicos/consultas.html')

def viewTelemedicina(request):
    return render(request, 'servicos/telemedicina.html')

@login_required(login_url='/acesso-paciente')
def viewResultadoExame(request):
    return render(request, "resultadoexame.html", {})


#REGISTER AND LOGIN
     
def viewRegister(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'user/register.html', {'form_usuario': form_usuario})


def viewLoginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'user/login.html', {'form_login': form_login})


@login_required(login_url='/acesso-paciente')
def viewLogout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/acesso-paciente')
def viewAlterarSenha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'user/alterarSenha.html', {'form_senha': form_senha})
