from django.db import models


class Client(models.Model):
    username = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    token = models.CharField(max_length=256, default="")
    token_generation_time = models.DateTimeField(auto_now=True)


class Admin(models.Model):
    username = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    token = models.CharField(max_length=256, default="")
    token_generation_time = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    book_id = models.AutoField(primary_key=True)
