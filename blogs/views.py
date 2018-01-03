from django.http import HttpResponse
from blogs.models import Blog, Post
from django.shortcuts import render


def home(request):
    latest_posts = Post.objects.all().order_by("created_at")
    context = {'posts': latest_posts}
    return render(request, "home.html", context)


def blogs(request):
    list_of_blogs = Blog.objects.all().order_by("created_at")
    context = {'blogs': list_of_blogs}
    return render(request, "blogs.html", context)
