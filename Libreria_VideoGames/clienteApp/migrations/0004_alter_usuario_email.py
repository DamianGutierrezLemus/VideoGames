# Generated by Django 5.1 on 2024-11-08 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clienteApp', '0003_alter_usuario_managers_usuario_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
