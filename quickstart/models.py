from django.db import models


# Author model (Many Authors can write Many Articles)
class Author(models.Model):
    class Meta:
        db_table = "author"
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Article model (Many-to-Many with Authors, One-to-Many with Comments)
class Article(models.Model):
    class Meta:
        db_table = "article"
    title = models.CharField(max_length=200)
    content = models.TextField()
    authors = models.ManyToManyField(Author)  # Many-to-Many with Author
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# Comment model (One-to-Many relationship with Article)
class Comment(models.Model):
    class Meta:
        db_table = "comment"
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # One-to-Many
    text = models.TextField()

