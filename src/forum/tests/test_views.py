from django.test import TestCase
from django.urls import reverse


class TestPost_listView(TestCase):
    """Test the post_list view."""
    def setUp(self):
        # Prepare a response object.        
        self.response = self.client.get('/')

    def test_post_list_view(self):
        # Test that it returns the right template
        self.assertTemplateUsed(self.response, 'forum/posts_list.html')
        

    # that the templates contains a certian context