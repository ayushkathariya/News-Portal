from .models import Post
from django.views import View
from django.db.models import Q
from django.shortcuts import render, get_object_or_404


# Create your views here.
class HomePageView(View):
    def get(self, request):
        if request.GET.get("search"):
            query = request.GET.get("search")
            posts = Post.objects.filter(
                Q(title__icontains=query)
                | Q(content__icontains=query)
                | Q(content__icontains=query)
            )
            context = {"posts": posts}
            return render(request, "newsapp/home.html", context)

        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, "newsapp/home.html", context)


class NewsDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, "newsapp/news-detail.html", {"post": post})
