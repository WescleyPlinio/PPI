from django.db import models
from users.models import Profile, Curso, Vinculo
from PIL import Image

class Projeto(models.Model):
    titulo = models.CharField(max_length=80)
    resumo = models.TextField(max_length=2000)
    objetivo = models.TextField(max_length=2000)
    capa = models.ImageField('media/')
    pdf = models.FileField(blank=True, null=True)
    palavras_chave = models.CharField(max_length=200, blank=True, null=True)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE, related_name="projetos")
    orientados = models.ManyToManyField(Profile, related_name="projetos_orientados", blank=True)
    orientadores = models.ManyToManyField(Profile, related_name="projetos_orientadores", blank=True)
    criado_em = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.capa:
            img = Image.open(self.capa.path)
            img = img.resize((563, 375), Image.LANCZOS)
            img.save(self.capa.path)
    
class FotoProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField()

    def __str__(self):
        return f"Foto do projeto {self.projeto.titulo}"
    
class Comentario(models.Model):
    usuario = models.ForeignKey(Profile, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="comentarios",null=True)
    texto =  models.TextField(max_length=1000)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario.username} em {self.criado_em.strftime('%d/%m/%Y %H:%M'),{self.projeto.titulo}}"
    

