# Generated by Django 4.0.6 on 2022-07-06 18:16

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0039_doacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao',
            name='Cor',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None, verbose_name='Cor do fundo'),
        ),
    ]