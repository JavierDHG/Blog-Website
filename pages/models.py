from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    imagen_post = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name='Imagen')
    title = models.CharField(max_length=100, verbose_name='Titulo')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs', verbose_name='Autor')
    content = models.CharField(max_length=100000, verbose_name='Contenido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el:')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el:')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = models.CharField(max_length=1000, verbose_name='Contenido')
    slug = models.CharField(unique=True, max_length=150, verbose_name='URL amigable')
    visible = models.BooleanField(default=True, verbose_name='¿Visible?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el:')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el:')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'