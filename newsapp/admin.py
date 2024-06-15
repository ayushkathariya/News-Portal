from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "updated_at", "created_at")
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "category", "is_published")
    list_filter = ("is_published", "category", "created_at")
    search_fields = ("title", "content", "author")
