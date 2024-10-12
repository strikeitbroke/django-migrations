from django.contrib import admin

from quickstart.models import Category, Author, Comment, Article


# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Article)
