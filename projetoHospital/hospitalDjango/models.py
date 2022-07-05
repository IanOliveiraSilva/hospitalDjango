from tabnanny import verbose
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Medico(models.Model):
    Nome = models.CharField(max_length=100) 
    Especialidade = models.CharField(max_length=50)
    def __str__(self):
        return self.Nome
    class Meta:
        verbose_name_plural = "Médicos - Guia Médico"

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
    class Meta:
        verbose_name_plural = "Parceiros"

class Convenio(models.Model):
    NomeConvenio = models.CharField(max_length=100)
    FotoCovenio = models.ImageField(upload_to='Convenio', null=True, blank=True)
    def __str__(self):
        return self.NomeConvenio
    class Meta:
        verbose_name_plural = "Convenio"

class Diretoria(models.Model):
    NomeDiretoria = models.CharField(max_length=100)
    CargoDiretoria = models.CharField(max_length=50)
    FotoDiretoria = models.ImageField(upload_to='Diretoria', null=True, blank=True)
    def __str__(self):
        return self.NomeDiretoria
    class Meta:
        verbose_name_plural = "Diretoria"

class Premio(models.Model):
    NomePremio = models.CharField(max_length=100)
    FotoPremio = models.ImageField(upload_to='Premio', null=True, blank=True)
    def __str__(self):
        return self.NomePremio
    class Meta:
        verbose_name_plural = "Premios"

class Banner(models.Model):
    NomeBanner = models.CharField(max_length=100)
    FotoBanner = models.ImageField(upload_to='Banner', null=True, blank=True)
    def __str__(self):
        return self.NomeBanner
    class Meta:
        verbose_name_plural = "Banners"

class Transparencia(models.Model):
    NomeTransparencia = models.CharField(max_length=100)
    PdfTransparencia = models.FileField(upload_to='pdf/', null=True, blank=True)
    DataTransparencia = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.NomeTransparencia
    class Meta:
        verbose_name_plural = "Transparência"

class DiretoriaExecutiva(models.Model):
    NomeDiretorExecutivo = models.CharField(max_length=100)
    CargoDiretorExecutivo = models.CharField(max_length=50)
    FotoDiretorExecutivo = models.ImageField(upload_to='DiretoriaExecutiva', null=True, blank=True)
    def __str__(self):
        return self.NomeDiretorExecutivo
    class Meta:
        verbose_name_plural = "Diretoria Executiva"

class ConselhoDeliberativo(models.Model):
    NomeConselho = models.CharField(max_length=100)
    CargoConselho = models.CharField(max_length=50)
    FotoConselho = models.ImageField(upload_to='ConselhoDeliberativo', null=True, blank=True)
    def __str__(self):
        return self.NomeConselho
    class Meta:
        verbose_name_plural = "Conselho Deliberativo"
    
class FaleConosco(models.Model):
    NomeCompleto = models.CharField(max_length=100, blank=True, null=True)
    Email = models.EmailField(max_length=50, blank=True, null=True)
    NumeroRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    Telefone = models.CharField(validators = [NumeroRegex], max_length = 11, unique = True)
    Assunto = models.CharField(max_length=50, blank=False, null=True)
    Mensagem = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.NomeCompleto
    class Meta:
        verbose_name_plural = "Fale Conosco"
    
class Galeria(models.Model):
    Titulo = models.CharField(max_length=150, blank=False, null=False)
    Categoria = models.CharField(max_length=100, blank=False, null = False)
    Foto = models.ImageField(upload_to='Galeria', blank=False, null=True)
    Descricao = models.CharField(max_length=400, blank=True, null=True)
    Data = models.DateField(null=False, blank=False)
    def __str__(self):
        return super().__str__()
    class Meta:
        verbose_name_plural = "galeria"

class NossaMissao(models.Model):
    Titulo = models.CharField(max_length=150, blank=False, null=False)
    Missao = models.TextField(blank=False, null=False)
    PoliticadeQualidade = models.TextField(blank=False, null=False)
    Proposito = models.TextField(blank=False, null=False)
    Valores = models.TextField(blank=False, null=False)
    Visao = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.Titulo
    class Meta:
        verbose_name_plural = "Nossa Missão"

class InformacaoRodape(models.Model):
    Titulo = models.CharField(max_length=150, blank=False, null=False)
    Telefone = models.CharField(max_length = 14, unique = True)
    Rua = models.TextField(blank=False, null=False)
    Numero = models.CharField(max_length=5 ,blank=False, null=False)
    Bairro = models.CharField(max_length=80,blank=False, null=False)
    CEP = models.CharField(max_length = 9, unique = True)
    Cidade = models.CharField(max_length=50, blank=False, null = False)
    Estado = models.CharField(max_length=5, blank=False, null=False)
    def __str__(self):
        return self.Titulo
    class Meta:
        verbose_name_plural = "Informações Rodapé"

class RedesSociais(models.Model):
    Titulo = models.CharField(max_length=150, blank=False, null=False)
    Facebook = models.CharField(max_length = 300, blank=False,null=False)
    Twitter = models.CharField(max_length = 300, blank=False,null=False)
    Instagram = models.CharField(max_length = 300, blank=False,null=False)
    Youtube = models.CharField(max_length = 300, blank=False,null=False)
    def __str__(self):
        return self.Titulo
    class Meta:
        verbose_name_plural = "Redes Sociais"

class HistoriaHospital(models.Model):
    Titulo = models.CharField(max_length=150, blank=False, null=False)
    Conteudo = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.Titulo
    class Meta:
        verbose_name_plural = "Historia"

class Eventos(models.Model):
    Titulo = models.CharField(max_length=100, blank=False, null=False)
    DataInício = models.DateField('Data de Início', null=False, blank=False)
    HoraInício = models.TimeField('Hora de Início', null=True, blank=True)
    DataFim = models.DateField('Data final', null=True, blank=True)
    HoraFim = models.TimeField('Hora Final', null=True, blank=True)
    Informações = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.Titulo
    class Meta:
        verbose_name_plural = "Eventos"