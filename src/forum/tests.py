from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Post


class DirectUrlTests(TestCase):
    """ Testing the environment before creating model instances."""
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/new_post/')
        self.assertEqual(response.status_code, 200)


class PostTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='my dummy title', text='my_text',)

    def test_post_creation(self):
        # Test post is an instance of Post.
        self.assertTrue(isinstance(self.post, Post))
        # Test title is what should be.
        self.assertEqual(self.post.title, 'my dummy title')
        # Test string representation of post.
        self.assertEqual(str(self.post),'my dummy title')

    def test_post_list_view(self):
        url = reverse('forum:posts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_post_detail_view(self):
        url = reverse('forum:post_detail', kwargs={'post_id':self.post.id,
            'post_slug':self.post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)