from django.contrib import admin
from .models import Post, Like, Comment, CommentLike

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(CommentLike)
# Register your models here.
