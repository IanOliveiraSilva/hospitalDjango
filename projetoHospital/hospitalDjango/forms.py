from dataclasses import fields
from django import forms
from .models import Medico, Noticia

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['Nome', 'Especialidade']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['Titulo', 'Subtitulo', 'Imagem', 'Corpo', 'Detalhes']
        