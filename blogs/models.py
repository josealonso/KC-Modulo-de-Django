# from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    blog_name = models.CharField(max_length=60)
    author = models.CharField(max_length=40)
    photo = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # posts = ArrayField(models.ForeignKey(Post, on_delete=models.PROTECT))
    #  ArrayField cannot be used to relate classes
    # posts = models.ManyToManyField(Post, related_name='posts')

    def __str__(self):
        return self.blog_name


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    title = models.CharField(max_length=130)
    summary = models.TextField()
    content = models.TextField()
    image = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class User(models.Model):
    author = models.CharField(max_length=70)
    # posts = models.Post[]

    def __str__(self):
        return self.author

