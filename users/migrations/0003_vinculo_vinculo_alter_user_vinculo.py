# Generated by Django 5.1.1 on 2025-01-25 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_curso_alter_user_vinculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinculo',
            name='vinculo',
            field=models.CharField(default='Indefinido', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='vinculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.vinculo'),
        ),
    ]