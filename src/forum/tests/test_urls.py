from django.test import TestCase, client
from django.urls import reverse, resolve
from forum.views import posts_list, post_detail, new_post, delete_post, reply
from forum.models import Post


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

    def test_delete_post_reverse(self):
        # Test reverse function.
        url = reverse('forum:delete_post', kwargs={'post_id':1, 'post_slug':'sluggish'})
        self.assertEqual(url, '/1/sluggish/delete/')

    def test_delete_post_resolve(self):
        # Test resolve function.
        match = resolve('/1/slug/delete/')
        self.assertEqual(match.func, delete_post)
    
    def test_delete_post_GET(self):
        # Test delete post GET request.
        url = reverse('forum:delete_post', kwargs={'post_id':1, 'post_slug': 'my-title'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_delete_post_POST(self):
        # Test delete non-existent post POST request.
        url = reverse('forum:delete_post', kwargs={'post_id': 2, 'post_slug': 'my-title'})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)

    def test_delete_real_post_POST(self):
        # Test delete existent post POST request.
        url = reverse('forum:delete_post', kwargs={'post_id': 1, 'post_slug': 'whatever'})
        response = self.client.post(url, {'delete': 'delete'})
        self.assertEqual(response.status_code, 302)
    
    def test_reply_GET_resolve(self):
        # Test resolve function retrieves correct function.
        res = resolve('/1/whatever/reply/')
        self.assertEqual(res.func, reply)

    def test_reply_GET_status_code(self):
        # Test get url status code.
        url = reverse('forum:reply', kwargs={'post_id': 1, 'post_slug': 'whatever'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_reply_POST_status_code(self):
        # Test post url status code.
        response = self.client.post('/1/whatever/reply/')
        self.assertEqual(response.status_code, 200)