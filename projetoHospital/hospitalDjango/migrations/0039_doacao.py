# Generated by Django 4.0.6 on 2022-07-06 18:15

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0038_rename_datainício_eventos_datainicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meio', models.CharField(max_length=100)),
                ('Imagem', models.ImageField(upload_to='Doacoes')),
                ('Informacoes', models.TextField(verbose_name='Informações')),
                ('Cor', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None)),
            ],
            options={
                'verbose_name_plural': 'Doações',
            },
        ),
    ]