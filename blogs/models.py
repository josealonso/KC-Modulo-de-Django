from django.db import models


class Blog(models.Model):
    blog_name = models.CharField(max_length=40)    # URLField()
    author = models.CharField(max_length=40)
    photo = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_name


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=130)
    summary = models.TextField()
    content = models.TextField()
    image = models.FileField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    # categories

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class User(models.Model):
    author = models.CharField(max_length=70)
    # posts = models.Post[]

    def __str__(self):
        return self.author

