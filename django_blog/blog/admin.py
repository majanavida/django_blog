from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    list_filter = ['created', 'title']
    prepopulated_fields = {'slug': ['title']}
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'date']
    list_filter = ['date']
    search_fields = ['user', 'body']