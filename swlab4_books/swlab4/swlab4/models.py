from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    book_id = models.AutoField(primary_key=True)
