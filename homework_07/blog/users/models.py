from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name="name", max_length=64, null=False)
    bio = models.TextField(verbose_name="bio", blank=True)
    age = models.PositiveIntegerField(default=1)


class Friend(models.Model):
    user = models.ForeignKey(User, related_name="user_id", on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name="friend_id", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
