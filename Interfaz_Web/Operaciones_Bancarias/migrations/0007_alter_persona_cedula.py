# Generated by Django 4.0.6 on 2022-08-09 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operaciones_Bancarias', '0006_prestamo_divisa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Cedula',
            field=models.PositiveBigIntegerField(max_length=11),
        ),
    ]
