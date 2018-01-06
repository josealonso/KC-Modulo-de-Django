from django.contrib import admin

# Register your models here.
from blogs.models import Blog
from blogs.models import Post, Category


admin.site.site_header = "Blogs Administration"
admin.site.site_title = admin.site.site_header

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Post)
