from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required






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



def viewLogout(request):
    logout(request)
    return redirect('home')
