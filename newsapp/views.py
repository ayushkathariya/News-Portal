from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post


# Create your views here.
class HomePageView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, "newsapp/home.html", context)


class NewsDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, "newsapp/news-detail.html", {"post": post})
