from django.db import models

class Usuario1(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.nome

class Usuario2(models.Model):
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
    descricao = models.TextField(max_length=120)
    resumo = models.TextField(max_length=2000)
    capa = models.ImageField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    usuarios1 = models.ManyToManyField(Usuario1)
    usuarios2 = models.ManyToManyField(Usuario2)
    
    def __str__(self):
        return self.titulo
    
class FotoProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField()

    def __str__(self):
        return f"Foto do projeto {self.projeto.titulo}"