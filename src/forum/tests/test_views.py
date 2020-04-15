from django.test import TestCase
from django.urls import reverse
from forum.models import Post


class Test_Posts_listView(TestCase):
    """Test the post_list view."""
    @classmethod
    def setUpTestData(cls):
        # Create 13 posts.
        nr_of_posts = 5
        for post_id in range(nr_of_posts):
            Post.objects.create(
                title = f'post {post_id}',
                text = f'text {post_id}',
            )

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


class Test_Post_Detail_view(TestCase):
    """Test the post_detail view."""
    def setUp(self):
        # Prepare a response object.
        Post.objects.create(title='some slug')
        url = reverse('forum:post_detail', kwargs={'post_id':1, 'post_slug': 'some-slug'})
        self.response = self.client.get(url)

    def test_post_detail_view_template(self):
        # Test that it returns the right template
        self.assertTemplateUsed(self.response, 'forum/post_detail.html')

    def test_post_detail_view_context(self):
        # Test that it returns the right context.
        self.assertIn('post', self.response.context)


class Test_New_Post_view_GET(TestCase):
    """Test the new_post view GET method."""
    def setUp(self):
        # Prepare a response object.
        url = '/new_post/'
        self.response = self.client.get(url)

    def test_new_post_view_template(self):
        # Test that it returns the right template
        self.assertTemplateUsed(self.response, 'forum/new_post_form.html')

    def test_new_post_view_context(self):
        # Test that it returns the right context.
        self.assertIn('form', self.response.context)


class Test_New_Post_view_POST(TestCase):
    """Test the new_post view POST method."""
    def setUp(self):
        # Prepare a response object.
        self.response = self.client.post('/new_post/', {'title': 'portobello', 'text':'my text'})

    def test_new_post_view_object_created(self):
        # Test that the correct object has been created.
        new_post = Post.objects.get(id=1)
        self.assertEqual(new_post.title, 'portobello')


class Test_Delete_Post_view_POST(TestCase):
    """Test the delete_post view POST method"""
    def setUp(self):
        # Create a post.
        Post.objects.create(title='test title', text='my text')
    
    def test_delete_post_view(self):
        # test post is present.
        my_post = Post.objects.get(id=1)
        self.assertEqual(my_post.title, 'test title')
        self.assertFalse(len(Post.objects.all()) == 0)
        # delete post.
        my_post.delete()
        # test post is gone.
        self.assertTrue(len(Post.objects.all()) == 0)

"""Here missing: delete post with replies raises 404 response."""

class Test_Reply_view_GET(TestCase):
    """Test the GET method of the reply view."""
    @classmethod
    def setUpTestData(cls):
        # We create a post in the fake database.
        Post.objects.create(title='my unused title', text='myoh')

    def setUp(self):
        # Setting up the response for all tests.
        self.response = self.client.get('/1/whatever/reply/') # it does not use the slug but hey... it works.

    def test_template_used(self):
        # Test that the correct html template has been used.
        self.assertTemplateUsed(self.response, 'partials/partial_reply_form.html')

    def test_text_in_template(self):
        # Test that certain words are in the template.
        self.assertContains(self.response, 'Submit reply')

    def test_reply_view_context(self):
        # Test contained in the response context.
        self.assertIn('form', self.response.context)
        self.assertNotIn('uetti', self.response.context)


class Test_Reply_view_POST(TestCase):
    """Test the POST method of the reply view."""
    @classmethod
    def setUpTestData(cls):
        # Create a post to use for all tests.
        Post.objects.create(title='lumpsum', text='pippo')

    def test_invalid_form_template_used(self):
        # Tests when form.is_valid == false.
        response = self.client.post('/1/whatever/reply/')
        # Test template used.
        self.assertTemplateUsed(response, 'partials/partial_reply_form.html')  
        # Test that the response content is not an empty string.      
        decoded_content = (response.content).decode('utf-8')
        self.assertTrue(decoded_content != '')
    
    def test_valid_form_empty_response(self):
        # Tests when form.is_valid == true.
        response = self.client.post('/1/whateer/reply/', {'title':'cip cip', 'text': 'my text'})
        # Test that the response content is an empty string.
        decoded_content = (response.content).decode('utf-8')
        self.assertTrue(decoded_content == '')
        # Test that the database contains 2 records.
        posts = Post.objects.all()
        self.assertEqual(len(posts), 2)
        self.assertTrue(len(posts) < 3)
        # Test that the new post is saved.
        new_post = Post.objects.get(pk=2)
        self.assertEqual(new_post.title, 'cip cip')
        # Test that the new post is a reply to post nr 1.
        self.assertEqual(new_post.ref_post.pk, 1)