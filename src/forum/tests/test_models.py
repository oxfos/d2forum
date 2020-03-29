from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify
from forum.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.post = Post.objects.create(title='my dummy title', text='my_text',)

    def test_post_creation(self):
        # Test post is an instance of Post.
        self.assertTrue(isinstance(self.post, Post))
        # Test title is what should be.
        self.assertEqual(self.post.title, 'my dummy title')
        # Test string representation of post.
        self.assertEqual(str(self.post),'my dummy title')
        # Test slug.
        my_slug = slugify(self.post.title)
        self.assertEqual(self.post.slug, my_slug)