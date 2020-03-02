from django.test import TestCase, client


class DirectUrlTests(TestCase):
    """ Testing the environment before creating model instances."""
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/new_post/')
        self.assertEqual(response.status_code, 200)