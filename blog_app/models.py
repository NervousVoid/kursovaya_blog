from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    text = models.CharField(max_length=100000)
    date = models.DateTimeField(auto_now_add=True)

    liked_users = [models.ForeignKey(User, on_delete=models.CASCADE)]
    rating = models.IntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)
    post_id = models.IntegerField()
