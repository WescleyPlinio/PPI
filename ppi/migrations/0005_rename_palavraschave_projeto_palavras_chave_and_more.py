# Generated by Django 5.1.1 on 2025-01-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppi', '0004_rename_usuario1_aluno_rename_usuario2_orientador_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='palavrasChave',
            new_name='palavras_chave',
        ),
        migrations.AlterField(
            model_name='projeto',
            name='alunos',
            field=models.ManyToManyField(related_name='projetos', to='ppi.aluno'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='orientadores',
            field=models.ManyToManyField(related_name='projetos', to='ppi.orientador'),
        ),
    ]