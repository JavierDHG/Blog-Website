from django.db import models
from django.contrib.auth.models import User
from pages.models import Blog

# Create your models here.

class Mis_Posts(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='mis_posts')

    def __str__(self):
        return  (f"Post de {self.blog.titulo}")
    
    class Meta:
        verbose_name = 'Mis Posts'
        verbose_name_plural = 'Mis Posts'

class Comentarios(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField(max_length=250)

    def __str__(self):
        return (f"Comentario de {self.autor.name} en el post {self.blog.title}")
    
    class Meta:
        verbose_name = 'Comentarios'
        verbose_name_plural = 'Comentarios'