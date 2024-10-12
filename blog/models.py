from django.db import models


# article model (many-to-many with authors, one-to-many with comments)
class Article(models.Model):
    class Meta:
        db_table = "blog_article"
    title = models.CharField(max_length=200)
    content = models.TextField()
    authors = models.ManyToManyField('quickstart.Author', related_name='authors_to_%(app_label)s_%(class)s')  # Many-to-Many with Author
    category = models.ForeignKey('quickstart.Category', related_name='category_to_%(app_label)s_%(class)s', on_delete=models.CASCADE)
