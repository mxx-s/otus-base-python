from django.test import TestCase
from .models import Post
from users.models import User

# Create your tests here.
class TestPost(TestCase):

    # перед каждым тестом
    def setUp(self) -> None:
        self.user = User.objects.create(name='user', age=2)
        self.post = Post.objects.create(title='test_title', body='this is body for test', autor=self.user)
        return super().setUp()

    # после каждого теста
    def tearDown(self) -> None:
        return super().tearDown()

    def test_str(self):
        # user = User.objects.create(name='user', age=2)
        # post = Post.objects.create(title='test_title', body='this is body for test', autor=user)
        # assert str(post) == 'test_title'
        # post = Post.objects.all().first()
        self.assertEqual(str(self.post), self.post.title)


    def test_exception_method(self):
        # user = User.objects.create(name='user', age=2)
        # post = Post.objects.create(title='test_title', body='this is body for test', autor=user)
        with self.assertRaises(NotImplementedError):
            self.post.exception_method()