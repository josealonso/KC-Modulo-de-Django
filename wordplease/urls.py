from django.contrib import admin
from django.urls import path, re_path

from users.views import LoginView, logout
from blogs.views import home, blogs, post_detail, my_posts, CreatePostView, MyPostsView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', LoginView.as_view(), name="login_page"),
    path('logout', logout, name="logout_page"),

    # re_path('^blogs/(?P<username>\w+)/$', MyPostsView.as_view(), name='my_posts_page'),
    path('blogs/<username>/', my_posts, name="my_posts_page"),
    # re_path('^blogsaBB/(?P<username>[a-z]+)/$', my_posts, name="my_posts_page"),
    path('blogs/', blogs, name='blogs_page'),
    path('new-post/', CreatePostView.as_view(), name="create_post_page"),
    path('posts/<int:pk>', post_detail, name="post_detail_page"),
    path('', home, name="home_page")
]
