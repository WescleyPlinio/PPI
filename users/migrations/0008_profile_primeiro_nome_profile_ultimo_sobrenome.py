# Generated by Django 5.1.1 on 2025-01-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='primeiro_nome',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='ultimo_sobrenome',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]