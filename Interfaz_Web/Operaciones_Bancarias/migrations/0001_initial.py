# Generated by Django 4.0.6 on 2022-07-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dirección', models.CharField(max_length=100)),
                ('Nombre', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cédula', models.DecimalField(decimal_places=1, max_digits=11)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
