from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Medico(models.Model):
    Nome = models.CharField(max_length=100) 
    Especialidade = models.CharField(max_length=50)
    def __str__(self):
        return self.Nome

class Noticia(models.Model):
    Titulo = models.CharField(max_length=100, )
    Subtitulo = models.CharField(max_length=100, blank=True)
    Imagem = models.ImageField(upload_to='Noticia',null=True, blank=True)
    Corpo = models.TextField(null=True, blank=True)
    Detalhes = models.TextField(null=True, blank=True)  
    Data = models.DateField(null=True)
    def __str__(self):
        return self.Titulo

class Parceiros(models.Model):
    NomeParceiro = models.CharField(max_length=50)
    FotoParceiro = models.ImageField(upload_to='parceiro', null=True)
    def __str__(self):
        return self.NomeParceiro

class Convenio(models.Model):
    NomeConvenio = models.CharField(max_length=100)
    FotoCovenio = models.ImageField(upload_to='Convenio', null=True, blank=True)
    def __str__(self):
        return self.NomeConvenio

class Diretoria(models.Model):
    NomeDiretoria = models.CharField(max_length=100)
    CargoDiretoria = models.CharField(max_length=50)
    FotoDiretoria = models.ImageField(upload_to='Diretoria', null=True, blank=True)
    def __str__(self):
        return self.NomeDiretoria

class Premio(models.Model):
    NomePremio = models.CharField(max_length=100)
    FotoPremio = models.ImageField(upload_to='Premio', null=True, blank=True)
    def __str__(self):
        return self.NomePremio

class Banner(models.Model):
    NomeBanner = models.CharField(max_length=100)
    FotoBanner = models.ImageField(upload_to='Banner', null=True, blank=True)
    def __str__(self):
        return self.NomeBanner

class Transparencia(models.Model):
    NomeTransparencia = models.CharField(max_length=100)
    PdfTransparencia = models.FileField(upload_to='pdf/', null=True, blank=True)
    DataTransparencia = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.NomeTransparencia

class DiretoriaExecutiva(models.Model):
    NomeDiretorExecutivo = models.CharField(max_length=100)
    CargoDiretorExecutivo = models.CharField(max_length=50)
    FotoDiretorExecutivo = models.ImageField(upload_to='DiretoriaExecutiva', null=True, blank=True)
    def __str__(self):
        return self.NomeDiretorExecutivo

class ConselhoDeliberativo(models.Model):
    NomeConselho = models.CharField(max_length=100)
    CargoConselho = models.CharField(max_length=50)
    FotoConselho = models.ImageField(upload_to='ConselhoDeliberativo', null=True, blank=True)
    def __str__(self):
        return self.NomeConselho
    
class FaleConosco(models.Model):
    Operadora = (
        ('TIM', 'Tim'),
        ('VIVO', 'Vivo'),
        ('CLARO', 'Claro'),
    )
    Nome = models.CharField(max_length=50, blank=False,)
    Sobrenome = models.CharField(max_length=50, blank=False)
    NumeroRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    Telefone = models.CharField(validators = [NumeroRegex], max_length = 11, unique = True)
    operadora = models.CharField(max_length=5, choices=Operadora, blank=False, null=True)
    Assunto = models.CharField(max_length=50, blank=True, null=True)
    Mensagem = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.Nome
    