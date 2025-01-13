from django.db import models
from django.contrib.auth.models import User

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
    resumo = models.TextField(max_length=150)
    objetivo = models.TextField(max_length=2000)
    capa = models.ImageField('media/')
    pdf = models.FileField(blank=True, null=True)
    imagens = models.ImageField(blank=True, null=True)
    palavras_chave = models.CharField(max_length=200, blank=True, null=True)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno, related_name="projetos")
    orientadores = models.ManyToManyField(Orientador, related_name="projetos")
    criado_em = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="comentarios",null=True)
    texto =  models.TextField(max_length=1000)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario.username} em {self.criado_em.strftime('%d/%m/%Y %H:%M'),{self.projeto.titulo}}"
    
class FotoProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField()

    def __str__(self):
        return f"Foto do projeto {self.projeto.titulo}"