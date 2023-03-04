from django.core.management.base import BaseCommand, CommandError
from posts.models import Post, Comment, Likes
from users.models import User, Friend


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        # create, update, delete, выборка всех объектов, выборка 1 объекта
        # filter
        # 1. DELETE
        print('Start')
        print('Удаляем старые данные')
        User.objects.all().delete()
        Friend.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()
        Likes.objects.all().delete()

        # 2. Создание
        print('Создаю новые данные')
        first_user = User.objects.create(name="First", age=22)
        second_user = User.objects.create(name="second", age=32)
        third_user = User.objects.create(name="third", age=25)
        first_friend = Friend.objects.create(user=first_user, friend=second_user)
        second_friend = Friend.objects.create(user=first_user, friend=third_user)
        third_friend = Friend.objects.create(user=third_user, friend=second_user)
        print(first_user.name)
        print(second_user.name)
        # 3. Обновление
        print('Обновляю')
        second_user.bio = 'Разработчик'
        second_user.save()
        print(second_user.bio)

        post = Post.objects.create(title="My first post", body="Hello, world", autor=first_user)
        post2 = Post.objects.create(title="My second post", body="Hello, world2", autor=third_user)
        post3 = Post.objects.create(title="My third post", body="Hello, world3", autor=second_user)
        print(post)
        print(post2)
        print(post3)

        print("comments")
        comment = Comment.objects.create(body="Lol, kek",post=post,author=first_user)
        comment2 = Comment.objects.create(body="Cheburek",post=post,author=first_user)
        comment3 = Comment.objects.create(body="Lmao",post=post,author=second_user)

        print(comment, comment2, comment3)

        print('likes')

        like = Likes.objects.create(user=first_user, post=post)
        like = Likes.objects.create(user=third_user, post=post)
        like = Likes.objects.create(user=second_user, post=post)

        print('End')