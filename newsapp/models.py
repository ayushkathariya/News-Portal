from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )
    featured_image = models.ImageField(upload_to="posts/images/", blank=True, null=True)
    is_published = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
