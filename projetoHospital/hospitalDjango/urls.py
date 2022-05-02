from django.urls import path

from .views import viewHome, viewParceiros, viewNoticias, viewContato, viewRegister,viewLoginUser, viewLogout, viewResultadoExame, viewquemSomos, vieweventos, viewservicos, viewdoacao, viewAlterarSenha
urlpatterns = [
    path('', viewHome, name='home'),
    path('parceiros/', viewParceiros, name='parceiros'),
    path('noticias/', viewNoticias, name='noticias'),
    path('contatos/', viewContato, name='contatos'),
    path('registrar-paciente', viewRegister, name="register-user"),
    path('acesso-paciente', viewLoginUser, name="login-user"),
    path('sair-da-conta', viewLogout, name="logout-user"),
    path('resultado-exame', viewResultadoExame, name="resultado-exame"),
    path('quem-somos', viewquemSomos, name="quem-somos"),
    path('eventos', vieweventos, name="eventos"),
    path('servicos', viewservicos, name="servicos"),
    path('doacao', viewdoacao, name="doacao"),
    path('alterar-senha', viewAlterarSenha, name="alterar-senha"),
    ]

