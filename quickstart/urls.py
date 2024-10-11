from django.urls import path
from .views import AuthorListView, ArticleListView, ArticleByAuthorView


urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/author/<str:name>/', ArticleByAuthorView.as_view(), name='article-by-author-name'),
]
