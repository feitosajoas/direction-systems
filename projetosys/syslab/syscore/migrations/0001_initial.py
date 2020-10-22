# Generated by Django 3.1 on 2020-08-18 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, verbose_name='Nome completo')),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('usuario', models.CharField(blank=True, max_length=30, verbose_name='Usuário')),
                ('senha', models.CharField(blank=True, max_length=18, verbose_name='Senha')),
                ('email', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=15)),
            ],
        ),
    ]