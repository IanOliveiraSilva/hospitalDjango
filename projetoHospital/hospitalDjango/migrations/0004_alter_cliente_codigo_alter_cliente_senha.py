# Generated by Django 4.0.4 on 2022-04-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0003_alter_cliente_codigo_alter_cliente_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.IntegerField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='senha',
            field=models.IntegerField(default='SOME STRING', max_length=200),
        ),
    ]
