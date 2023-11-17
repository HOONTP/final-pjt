from django.contrib import admin
from .models import Article, Comment, Reply, Board

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Board)
