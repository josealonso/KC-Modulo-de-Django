from django.contrib import admin
from django.urls import path

from blogs.api import BlogsListAPI
from blogs.views import home, blogs, post_detail, my_posts, CreatePostView, UserPostsView
from users.views import LoginView, logout, SignupView
from users.api import HelloWorld, UsersListAPI, UserDetailAPI

# from blogs.views import blogs_list

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', LoginView.as_view(), name="login_page"),
    path('logout', logout, name="logout_page"),
    path('signup', SignupView.as_view(), name="signup_page"),

    # path('^blogs/(?P<username>\w+)/$', MyPostsView.as_view(), name='my_posts_page'),
    path('blogs/<slug:username>', UserPostsView.as_view(), name="user_posts_page"),
    path('blogs/<slug:username>/<int:pk>', post_detail, name="post_detail_page"),
    path('blogs/', blogs, name='blogs_page'),
    path('new-post/', CreatePostView.as_view(), name="create_post_page"),
    path('', home, name="home_page"),

    # API REST
    path('api/1.0/hello', HelloWorld.as_view(), name="api_hello_world"),
    path('api/1.0/users/<slug:pk>', UserDetailAPI.as_view(), name="api_users_detail"),
    path('api/1.0/users', UsersListAPI.as_view(), name="api_users_list"),
    path('api/1.0/blogs', BlogsListAPI.as_view(), name="api_blogs_list")
]
