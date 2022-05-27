from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import *

# READ - GUIA MÉDICO

def viewGuiaMedico(request):
    medico = Medico.objects.all()
    return render(request, "guiaMedico.html", {"medico": medico})

# READ - NOTICIAS

def viewNoticia(request):
    noticia = Noticia.objects.all()
    return render(request, "noticias.html", {"noticia": noticia})


# READ - PARCEIROS

def viewParceiros(request):
    parceiro = Parceiros.objects.all()
    return render(request, "parceiros.html", {"parceiro": parceiro})

# READ - CONVENIOS

def viewConvenio(request):
    convenio = Convenio.objects.all()
    return render(request, "convenio.html", {"convenio": convenio})

# READ - DIRETORIA E HISTORIA HOSPITAL LAUREANO

def viewDiretoria(request):
    diretoria = Diretoria.objects.all()
    return render(request, "diretoria.html", {"diretoria": diretoria})

def viewHistoriaHospital(request):
    return render(request, "historiaHospital.html", {})

# READ - DIRETORIA E HISTORIA FUNDAÇÃO Laureano

def viewHistoriaFundacao(request):
    return render(request, "historiaFundacao.html", {})

def viewDiretoriaFundacao(request):
    return render(request, "diretoriaFundacao.html", {})


# READ - PREMIOS E CERTIFICAÇÕES

def viewPremio(request):
    premio = Premio.objects.all()
    return render(request, "premio.html", {"premio": premio})

# READ - TRANSPARÊNCIA

def viewTransparencia(request):
    transparencia = Transparencia.objects.all()
    return render(request, "transparencia.html", {"transparencia": transparencia})




#PATH

def viewHome(request):
    banner = Banner.objects.all()
    premio = Premio.objects.all()
    noticia = Noticia.objects.all()
    convenio = Convenio.objects.all()
    
    return render(request, "home.html", {"banner": banner , "noticia": noticia, "premio": premio, "convenio": convenio})


def vieweventos(request):
    return render(request, "eventos.html", {})

def viewdoacao(request):
    return render(request, "doacao.html", {})

def viewNossaMissao(request):
    return render(request, "nossaMissao.html")


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
