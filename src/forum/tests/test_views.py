from django.test import TestCase
from django.urls import reverse


class TestPosts_listView(TestCase):
    """Test the post_list view."""
    def setUp(self):
        # Prepare a response object.        
        self.response = self.client.get('/')

    def test_posts_list_view_template(self):
        # Test that it returns the right template
        self.assertTemplateUsed(self.response, 'forum/posts_list.html')

    def test_posts_list_view_text_in_template(self):
        # Test that a certain text is in the returned template.
        self.assertContains(self.response, 'These')

    def test_posts_list_view_context(self):
        # Test that a certain term is in the response context.
        self.assertIn('posts', self.response.context)