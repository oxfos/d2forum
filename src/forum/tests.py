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

    def test_post_list_url(self):
        # Test namespace works.
        url = reverse('forum:posts_list')
        self.assertEqual(url, '/')
    
    def test_post_list_status(self):
        # Test request to posts list works.
        url = reverse('forum:posts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_post_detail_url(self):
        # Test namespace works.
        url = reverse('forum:post_detail', kwargs={'post_id':self.post.id,
            'post_slug':self.post.slug})
        url_str = f'/{self.post.id}/{self.post.slug}'
        self.assertEqual(url, url_str)
    
    def test_post_detail_status(self):
        # Test request to post_detail works.
        url = reverse('forum:post_detail', kwargs={'post_id':self.post.id,
            'post_slug':self.post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_post_namespace(self):
        # Test namespace new_post works.
        url = reverse('forum:new_post')
        self.assertEqual(url, '/new_post/')
    
    def test_new_post_status(self):
        # Test GET request to new_post works.
        url = reverse('forum:new_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_post_POST(self):
        # Test POST request to new_post works.
        url = reverse('forum:new_post')
        response = self.client.post(url, {'title': 'my post',
         'text': 'whatever text'}, follow=True) # follow=True ensures redirect is followed
        self.assertEqual(response.status_code, 200)