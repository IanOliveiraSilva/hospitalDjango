# Generated by Django 4.0.5 on 2022-06-04 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0025_remove_faleconosco_nome_remove_faleconosco_sobrenome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faleconosco',
            name='operadora',
        ),
    ]
