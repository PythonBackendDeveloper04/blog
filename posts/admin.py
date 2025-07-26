from django.contrib import admin
from .models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'status']
    prepopulated_fields = {"slug": ('title',)}

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_at']
    search_fields = ['user', 'body']

admin.site.register(Comment, CommentAdmin)