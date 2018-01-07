from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

from django.utils.safestring import mark_safe
from django.views import View
from django.views.generic import ListView

from blogs.models import Blog, Post, User
from blogs.templates.forms import PostForm


@login_required
def home(request):
    latest_posts = Post.objects.all().order_by("created_at")
    context = {'posts': latest_posts}
    return render(request, "home.html", context)


class CreatePostView(LoginRequiredMixin, View):

    def get(self, request, pk):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})

    def post(self, request, pk=9):
        post = Post()
        post.user = request.user
        post.id = pk
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_page", args=[post.user, post.pk])
            message = "¡¡ Se ha creado una nueva entrada !!"
            message += '<a href="{0}">Ver</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})


def blogs(request):
    list_of_blogs = Blog.objects.all().order_by("created_at")
    # list_of_blogs = User.objects.filter(blog=)  # .select_related("category")
    list_of_users = User.objects.all()
    context = {'users': list_of_users, 'blogs': list_of_blogs}
    return render(request, "blogs.html", context)


@login_required
def post_detail(request, username, pk):
    list_of_posts = Post.objects.filter(user=request.user, pk=pk)  # .select_related("category")
    blog = Post.objects.filter(pk=pk).select_related("blog")
    if len(list_of_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        post = list_of_posts[0]
        # blog = list_of_blogs[0]
        context = {'post': post, 'blog': blog}
        return render(request, "post_detail.html", context)


def my_posts(request, username):
    user = request.user
    # posts = Post.objects.filter(username=user)
    # user = username
    # posts = Post.objects.filter(user=username)  # ----> ValueError
    posts = Post.objects.filter(user=user)
    context = {'posts': posts, 'user': username}
    return render(request, "my_posts_page.html", context)


class MyPostsView(ListView):
    model = Post
    template_name = "my_posts_page.html"

    def get_queryset(self):
        # u = get_object_or_404(User, )
        queryset = super(MyPostsView, self).get_queryset()
        return queryset.filter(user=self.request.user)
