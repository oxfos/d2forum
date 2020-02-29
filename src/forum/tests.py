from django.test import TestCase
from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            'title'='test_title',
            'text'='my_text',
        )

    def test_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'test_title')