from django.db import models
from django.contrib.auth.models import AbstractUser

class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    logo = models.FileField(blank=True)
    
    def __str__(self):
        return self.titulo

class Vinculo(models.Model):
    vinculo = models.CharField(max_length=50, default="Indefinido")
    
    def __str__(self):
        return self.vinculo

class User(AbstractUser):
    vinculo = models.ForeignKey(Vinculo, on_delete=models.CASCADE, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    