# Generated by Django 4.0.5 on 2022-06-07 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0027_galeria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galeria',
            old_name='Descrição',
            new_name='Descricao',
        ),
    ]
