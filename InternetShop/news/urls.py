# from django.urls import path
# from . import views

# app_name = "news"

# urlpatterns = [
#     path('', views.news_page, name='news'),
# ]

from django.urls import path

from news.views import ArticleDetailView, ArticlesListView

urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="news_details"),
    path("", ArticlesListView.as_view(), name="news_page"),
]