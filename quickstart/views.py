from rest_framework import generics
from .models import Author, Article
from .serializers import AuthorSerializer, ArticleSerializer
from django.shortcuts import get_object_or_404


# Generic List API for Author
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Generic List API for Article
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleByAuthorView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        name = self.kwargs.get("name")
        author = get_object_or_404(Author, name=name)
        return author.article_set.all()
        
