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
    title = models.CharField(max_length=130)
    summary = models.TextField()
    body = models.TextField()
    publication_date = models.DateTimeField(default=datetime.datetime.now())
    image = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    # category = models.ManyToManyField(Category)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


