from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.nome

class Orientador(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    logo = models.FileField(blank=True)
    
    def __str__(self):
        return self.titulo

class Projeto(models.Model):
    titulo = models.CharField(max_length=80)
    resumo = models.TextField(max_length=120)
    objetivo = models.TextField(max_length=2000)
    capa = models.ImageField()
    pdf = models.FileField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)
    orientadores = models.ManyToManyField(Orientador)
    curso = models.CharField(max_length=80)
    palavrasChave = models.CharField(max_length=2000)

    
    def __str__(self):
        return self.titulo
    
class FotoProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField()

    def __str__(self):
        return f"Foto do projeto {self.projeto.titulo}"