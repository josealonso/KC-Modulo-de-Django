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


def post_detail(request, pk):
    list_of_posts = Post.objects.filter(pk=pk)  # .select_related("category")
    if len(list_of_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        post = list_of_posts[0]
        context = {'post': post}
        return render(request, "post_detail.html", context)