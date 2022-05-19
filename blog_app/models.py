from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    text = models.CharField(max_length=100000)
    date = models.DateTimeField(auto_now_add=True)
    liked_users = models.ManyToManyField(User, related_name='liked_users')

    def get_rating(self):
        return self.liked_users.all().count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=512)
    post_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


def get_user_rating(self):
    rating = 0
    posts = self.post.all()
    for each in posts:
        rating += each.get_rating()
    return rating


User.add_to_class('user_rating', get_user_rating)

