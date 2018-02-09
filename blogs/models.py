from django.contrib.auth.models import User
from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=130, verbose_name="Título")
    summary = models.TextField(verbose_name="Resumen")
    body = models.TextField(verbose_name="Cuerpo")
    publication_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name="Fecha de publicación")
    image = models.URLField(blank=True, null=True, verbose_name="Imagen")
    video = models.URLField(blank=True, null=True, verbose_name="Vídeo")
    # category = models.ManyToManyField(Category)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


