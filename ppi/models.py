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

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    justificativa = models.TextField(max_length=120)
    resumo = models.TextField(max_length=2000)
    data_publi = models.DateField(auto_now=True)
    usuarios1 = models.ManyToManyField(Usuario1)
    usuarios2 = models.ManyToManyField(Usuario2)

    def __str__(self):
        return self.titulo