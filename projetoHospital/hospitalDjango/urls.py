from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from .views import *
urlpatterns = [
    path('', viewHome, name='home'),
    path('parceiros/', viewParceiros, name='parceiros'),
    path('noticias/', viewNoticia, name='noticias'),
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
    path('guia-medico/', viewGuiaMedico, name="guia-medico"),
    path('administrar/', viewAdmin, name="administrar"),
    path('form-medico', viewAddMedico, name="form-medico"),
    path('update/<int:id>/', viewEditMedico, name="edit-medico"),
    path('delete/<int:id>/', viewDeleteMedico, name="delete-medico"),
    path('form-noticia', viewAddNoticia, name="form-noticia"),
    path('update/<int:id>/', viewEditNoticia, name="edit-noticia"),
    path('delete/<int:id>/', viewDeleteNoticia, name="delete-noticia"),
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)