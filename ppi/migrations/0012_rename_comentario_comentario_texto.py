# Generated by Django 5.1.1 on 2025-01-10 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppi', '0011_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='comentario',
            new_name='texto',
        ),
    ]
