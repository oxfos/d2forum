from django.test import TestCase, SimpleTestCase, client
from django.urls import reverse, resolve
from forum.views import posts_list, post_detail, new_post


class ForumUrlTests(SimpleTestCase):
    """Test forum urls."""
    def test_list_url_is_resolved(self):
        url = reverse('forum:posts_list')
        res = resolve(url)
        self.assertEqual(res.func, posts_list)

    def test_post_detail_is_resolved(self):
        url = reverse('forum:post_detail', kwargs={'post_id':1, 'post_slug': 'some-slug'})
        res = resolve(url)
        self.assertEqual(res.func, post_detail)

    def test_new_post_url_is_resolved(self):
        url = reverse('forum:new_post')
        res = resolve(url)
        self.assertEqual(res.func, new_post)


class DirectUrlTests(TestCase):
    """ Testing the environment before creating model instances."""
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/new_post/')
        self.assertEqual(response.status_code, 200)