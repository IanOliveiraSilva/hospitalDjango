# Generated by Django 4.0.4 on 2022-05-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0008_parceiros_nomeparceiro_alter_parceiros_fotoparceiro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diretoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomeDiretoria', models.CharField(max_length=100)),
                ('CargoDiretoria', models.CharField(max_length=50)),
                ('FotoDiretoria', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='parceiros',
            name='NomeParceiro',
            field=models.CharField(max_length=50),
        ),
    ]
