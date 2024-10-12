from django.contrib import admin
from quickstart.models import Category, Author, Article, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)

