# Generated by Django 4.0.4 on 2022-05-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalDjango', '0007_convenio_fotocovenio'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceiros',
            name='NomeParceiro',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='parceiros',
            name='FotoParceiro',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]