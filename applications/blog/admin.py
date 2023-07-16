from django.contrib import admin
from .models import Blog, Comment, Tags, Category, Post
# Register your models here.
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Post)