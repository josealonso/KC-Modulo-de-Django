from django.contrib import admin
from django.urls import path

from users.views import LoginView, logout
from blogs.views import home, blogs, post_detail, CreatePostView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', LoginView.as_view(), name="login_page"),
    path('logout', logout, name="logout_page"),
    path('blogs/', blogs, name='blogs_page'),
    path('new-post/', CreatePostView.as_view(), name="create_post_page"),
    path('posts/<int:pk>', post_detail, name="post_detail_page"),
    path('', home, name='home_page'),
]
