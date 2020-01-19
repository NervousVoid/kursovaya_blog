from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    text = models.CharField(max_length=100000)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
