from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *

urlpatterns = [
    # Páginas Principais
    path('', viewHome, name='home'),
    path('parceiros/', viewParceiros, name='parceiros'), 
    path('contatos/', viewContato, name='contatos'),
    path('resultado-exame', viewResultadoExame, name="resultado-exame"),
    path('quem-somos', viewquemSomos, name="quem-somos"),
    path('eventos', vieweventos, name="eventos"),
    path('servicos', viewservicos, name="servicos"),
    path('doacao', viewdoacao, name="doacao"),
    path('guia-medico/', viewGuiaMedico, name="guia-medico"),
    path('noticias/', viewNoticia, name='noticias'),
    
    # Login
    path('registrar-paciente', viewRegister, name="register-user"),
    path('acesso-paciente', viewLoginUser, name="login-user"),
    path('alterar-senha', viewAlterarSenha, name="alterar-senha"),
    path('sair-da-conta', viewLogout, name="logout-user"),
    
    # Admin
    path('administrar/', viewAdmin, name="administrar"),
    path('administrar/GuiaMedico', viewAdminGuiaMedico, name="admin-Guia-Medico"),
    path('administrar/Noticias', viewAdminNoticia, name="admin-Noticias"),

    # Forms
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
