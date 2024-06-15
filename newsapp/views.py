from django.shortcuts import render
from django.views import View


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, "newsapp/home.html")


class NewsDetailView(View):
    def get(self, request, slug):
        return render(request, "newsapp/news-detail.html", {"slug": slug})
