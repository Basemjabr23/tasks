from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'author',
        'is_published',
        'created_at'
    ]

    list_filter = ['category', 'is_published']
    search_fields = ['title']