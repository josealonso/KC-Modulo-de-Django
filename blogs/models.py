from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=60)
    image = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=130)
    summary = models.TextField()
    content = models.TextField()
    image = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class User(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    author = models.CharField(max_length=70)

    def __str__(self):
        return self.author

