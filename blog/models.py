from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = ResizedImageField(size=[800, 700],upload_to="blog", blank=True, null=True)
    content = RichTextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='rascunho')
    
    def get_absolut_url(self):
        return reverse('post_detail', args=[self.slug])

    class Meta:
        ordering = ('-publicado',)
    
    def __str__(self):
        return self.title

# Create your models here.
