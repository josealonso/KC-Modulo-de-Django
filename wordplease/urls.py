from django.contrib import admin
from django.urls import path, re_path

from users.views import LoginView, logout, SignupView
from blogs.views import home, blogs, post_detail, my_posts, CreatePostView, UserPostsView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', LoginView.as_view(), name="login_page"),
    path('logout', logout, name="logout_page"),
    path('signup', SignupView.as_view(), name="signup_page"),

    # re_path('^blogs/(?P<username>\w+)/$', MyPostsView.as_view(), name='my_posts_page'),
    path('blogs/<slug:username>/', UserPostsView.as_view(), name="user_posts_page"),
    path('blogs/<slug:username>/<int:pk>', post_detail, name="post_detail_page"),
    path('blogs/', blogs, name='blogs_page'),
    path('new-post/', CreatePostView.as_view(), name="create_post_page"),

    path('', home, name="home_page")
]
