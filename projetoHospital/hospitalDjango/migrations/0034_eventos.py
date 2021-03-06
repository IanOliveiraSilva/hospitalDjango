# Generated by Django 4.0.6 on 2022-07-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0033_historiahospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('Data', models.DateTimeField()),
                ('Duração', models.DurationField(blank=True, null=True, verbose_name='duração')),
                ('Informações', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
