from django.db import models


# Create your models here.


class Medico(models.Model):
    Nome = models.CharField(max_length=100) 
    Especialidade = models.CharField(max_length=50)
    def __str__(self):
        return self.Nome

class Noticia(models.Model):
    Titulo = models.CharField(max_length=100)
    Subtitulo = models.CharField(max_length=100)
    Imagem = models.ImageField(null=True, blank=True)
    Corpo = models.TextField()
    Detalhes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.Titulo

class Parceiros(models.Model):
    NomeParceiro = models.CharField(max_length=50)
    FotoParceiro = models.ImageField(null=True)
    def __str__(self):
        return self.NomeParceiro

class Convenio(models.Model):
    NomeConvenio = models.CharField(max_length=100)
    FotoCovenio = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.NomeConvenio
