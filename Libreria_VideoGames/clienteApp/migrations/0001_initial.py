# Generated by Django 5.1 on 2024-11-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_User', models.CharField(max_length=150)),
                ('Apellido_User', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('tarjeta_asociada', models.IntegerField()),
                ('Miembro', models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], max_length=3)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
