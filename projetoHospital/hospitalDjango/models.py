from django.db import models

# Create your models here.


class adicionarMedicos(models.Model):
    Nome = models.TextField() 
    Especializacao = models.TextField()
    class Meta:
        db_table = 'adicionarMedicos'
    def str(self):
        return self.id
    