from django.db import models


class Client(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    token = models.CharField(max_length=256, default="")
    token_generation_time = models.DateTimeField(auto_now=True)
