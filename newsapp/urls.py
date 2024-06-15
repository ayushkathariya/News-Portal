from django.urls import path
from .views import HomePageView, NewsDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("<str:slug>/", NewsDetailView.as_view(), name="news-detail"),
]
