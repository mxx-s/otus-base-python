from django.test import TestCase

class PostListView(TestCase):

    def test_responce(self):
        responce = self.client.get('/posts/')
        self.assertEqual(responce.status_code, 200)

    def test_responce_context(self):
        responce = self.client.get('/posts/')
        self.assertIn('help', responce.context)
        self.assertEqual(responce.context['help'], 'This is a help text')
        self.assertEqual(responce.status_code, 200)