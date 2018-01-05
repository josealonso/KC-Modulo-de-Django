from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

from django.utils.safestring import mark_safe
from django.views import View

from blogs.models import Blog, Post
from blogs.templates.forms import PostForm


@login_required
def home(request):
    latest_posts = Post.objects.all().order_by("created_at")
    context = {'posts': latest_posts}
    return render(request, "home.html", context)


class CreatePostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_page", args=[post.pk])
            message = "¡¡ Se ha creado una nueva entrada !!"
            message += '<a href="{0}">Ver</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})


def blogs(request):
    list_of_blogs = Blog.objects.all().order_by("created_at")
    context = {'blogs': list_of_blogs}
    return render(request, "blogs.html", context)


@login_required
def post_detail(request, pk):
    list_of_posts = Post.objects.filter(pk=pk)  # .select_related("category")
    blog = Post.objects.filter(pk=pk).select_related("blog")
    if len(list_of_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        post = list_of_posts[0]
        # blog = list_of_blogs[0]
        context = {'post': post, 'blog': blog}
        return render(request, "post_detail.html", context)
