from django.contrib import admin

from .models import User, Post, Theme, Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Theme)
admin.site.register(Comment)