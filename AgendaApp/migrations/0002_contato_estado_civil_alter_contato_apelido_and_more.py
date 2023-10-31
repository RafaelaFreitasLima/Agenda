# Generated by Django 4.2.6 on 2023-10-31 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='estado_civil',
            field=models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viúvo')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='apelido',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='complemento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='endereco',
            field=models.CharField(max_length=200, verbose_name='Endereço'),
        ),
    ]
