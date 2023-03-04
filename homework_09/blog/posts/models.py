from django.db import models

from users.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(verbose_name="title", max_length=20, null=False)
    body = models.TextField(verbose_name="body", blank=True)
    autor = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)

    def exception_method(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    body = models.TextField(verbose_name="text", max_length=64, null=False)
    post = models.ForeignKey(Post, verbose_name="post", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)


class Likes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
