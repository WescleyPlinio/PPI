# Generated by Django 5.1.1 on 2025-01-04 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppi', '0006_alter_projeto_capa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='images',
            new_name='imagens',
        ),
    ]