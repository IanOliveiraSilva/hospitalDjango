from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import Medico, Noticia
from .forms import MedicoForm, NoticiaForm

#CRUD - GUIA MÉDICO

# CREATE

def viewAddMedico(request):
    form = MedicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('administrar')
    return render(request, 'form-medico.html', {'form': form})

# UPDATE
def viewEditMedico(request, id):
    medico = Medico.objects.get(id=id)
    form = MedicoForm(request.POST or None, instance=medico)

    if form.is_valid():
        form.save()
        return redirect('administrar')
    return render(request, 'form-medico.html', {'form': form, 'medico': medico})

# DELETE
def viewDeleteMedico(request, id):
    medico = Medico.objects.get(id=id)
    if request.method == "POST":
        medico.delete()
        return redirect('administrar')
    return render(request, 'confirm-delete.html', {'medico': medico})

# VIEW






# CRUD - NOTICIAS

# CREATE

def viewAddNoticia(request):
    formNoticia = NoticiaForm(request.POST or None)

    if formNoticia.is_valid():
       formNoticia.save()
       return redirect('administrar')
    return render(request, 'form-noticia.html', {'form-noticia': formNoticia})

# UPDATE

def viewEditNoticia(request, id):
    noticia = Noticia.objects.get(id=id)
    formNoticia = NoticiaForm(request.POST or None, instance=noticia)

    if formNoticia.is_valid():
        formNoticia.save()
        return redirect('administrar')
    return render(request, 'edit-noticia.html', {'formNoticia': formNoticia, 'noticia': noticia})

# DELETE 

def viewDeleteNoticia(request, id):
    noticia = Noticia.objects.get(id=id)
    if request.method == 'POST':
        Noticia.delete()
        return redirect('administrar')
    return render(request, 'confirm-delete.html', {'noticia': noticia} )






# PERMISSAO PARA ADMIN

def viewAdmin(request):
   if not request.user.is_superuser:
       return HttpResponse('The user is not admin')
   else:
    medico = Medico.objects.all()
    return render(request, "administrar.html", {"medico": medico})




# Usuário Padrão
def viewGuiaMedico(request):
    medico = Medico.objects.all()
    return render(request, "guiaMedico.html", {"medico": medico})

def viewNoticia(request):
    noticia = Noticia.objects.all()
    return render (request, "noticias.html", {"noticia": noticia})


#PATH

def viewHome(request):
    return render(request, "home.html", {})


def viewParceiros(request):
    return render(request, "parceiros.html", {})


def viewNoticias(request):
    return render(request, "noticias.html", {})


def viewContato(request):
    return render(request, "contatos.html", {})

def viewquemSomos(request):
    return render(request, "quemSomos.html", {})

def viewservicos(request):
    return render(request, "servicos.html", {})

def vieweventos(request):
    return render(request, "eventos.html", {})

def viewdoacao(request):
    return render(request, "doacao.html", {})

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
    return render(request, 'register.html', {'form_usuario': form_usuario})


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
    return render(request, 'login.html', {'form_login': form_login})


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
    return render(request, 'alterarSenha.html', {'form_senha': form_senha})
