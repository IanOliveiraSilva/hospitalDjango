# Generated by Django 4.0.5 on 2022-06-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0024_alter_faleconosco_assunto_alter_faleconosco_mensagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faleconosco',
            name='Nome',
        ),
        migrations.RemoveField(
            model_name='faleconosco',
            name='Sobrenome',
        ),
        migrations.AddField(
            model_name='faleconosco',
            name='Email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='faleconosco',
            name='NomeCompleto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faleconosco',
            name='Assunto',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
