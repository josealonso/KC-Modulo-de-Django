from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from django.utils.safestring import mark_safe
from django.views import View
from django.views.generic import ListView

from blogs.models import Post
from blogs.templates.forms import PostForm
import datetime


@login_required
def home(request):
    latest_posts = Post.objects.all().order_by("-created_at")
    context = {'posts': latest_posts}
    return render(request, "home.html", context)


@login_required
def blogs(request):
    # list_of_blogs = Blog.objects.all().order_by("created_at")
    list_of_users = User.objects.all()
    context = {'users': list_of_users}  # 'blogs': list_of_blogs}
    return render(request, "blogs.html", context)


@login_required
def post_detail(request, username, pk):
    # list_of_posts = Post.objects.filter(pk=pk).select_related("user=username")
    #  Error: Invalid field name given in select_related
    list_of_posts = Post.objects.filter(pk=pk).select_related("user")
    if len(list_of_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        post = list_of_posts[0]
        # blog = list_of_blogs[0]
        context = {'post': post}
        return render(request, "post_detail.html", context)


def my_posts(request):    # Not used
    posts = Post.objects.filter(__username__exact=username)
    # posts = Post.objects.filter(user=username)  # ----> ValueError
    context = {'posts': posts, 'user': request.user}
    return render(request, "user_posts_page.html", context)


class CreatePostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})

    def post(self, request):
        post = Post()
        post.user = request.user
        # post.id = pk
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_page", args=[post.user.username, post.pk])
            message = "¡¡ Se ha creado una nueva entrada !!"
            message += '<a href="{0}">Ver</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})


class UserPostsView(ListView):
    model = Post
    template_name = "user_posts_page.html"

    def get_queryset(self):
        now = datetime.datetime.now()
        queryset = super(UserPostsView, self).get_queryset()
        username = self.kwargs.get("username")  # param. "username" declarado en "urls.py"
        user = get_object_or_404(User, username__iexact=username)
        return queryset.filter(user=user).order_by('-publication_date')

    def get_context_data(self, **kwargs):
        username = self.kwargs.get("username")
        context = super().get_context_data(**kwargs)
        context['username'] = username
        return context

