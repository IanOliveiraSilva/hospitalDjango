# Generated by Django 4.0.6 on 2022-07-06 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0040_alter_doacao_cor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doacao',
            name='Cor',
        ),
    ]
