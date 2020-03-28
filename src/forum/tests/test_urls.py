from django.test import TestCase, client
from django.urls import reverse, resolve
from forum.views import posts_list, post_detail, new_post
from ..models import Post


class ForumUrlTests(TestCase):
    """Test reverse and resolve urls."""
    def setUp(self):
        # Create Post object for test.
        self.post = Post.objects.create(title='my title', text='my text')

    def test_post_list_url(self):
        # Test link namespace > url > view function.
        url = reverse('forum:posts_list')
        self.assertEqual(url, '/')
        res  = resolve(url)
        self.assertEqual(res.func, posts_list)
        # Test get request.
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_is_resolved(self):
        # Test link namespace > url > view function.
        url = reverse('forum:post_detail', kwargs={'post_id':1, 'post_slug': 'my-title'})
        self.assertEqual(url, '/1/my-title')
        res = resolve(url)
        self.assertEqual(res.func, post_detail)
        # Test get request.
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) 

    def test_new_post_GET(self):
        # Test namespace > url > view function.
        url = reverse('forum:new_post')
        self.assertEqual(url, '/new_post/')
        res = resolve(url)
        self.assertEqual(res.func, new_post)
        # Test get request.
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
     
    def test_new_post_POST(self):
        # Test POST request to new_post works.
        url = reverse('forum:new_post')
        response = self.client.post(url, {'title': 'my post', 'text': 'whatever text'},
         follow=False) # follow=True ensures redirect is followed
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)