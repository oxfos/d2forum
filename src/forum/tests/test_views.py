from django.test import TestCase
from django.urls import reverse
from forum.models import Post


class TestPosts_listView(TestCase):
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


class TestPost_DetailView(TestCase):
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


class TestNew_Post_view_GET(TestCase):
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


class TestNew_Post_view_POST(TestCase):
    """Test the new_post view POST method."""
    def setUp(self):
        # Prepare a response object.
        self.response = self.client.post('/new_post/', {'title': 'portobello', 'text':'my text'})

    def test_new_post_view_object_created(self):
        # Test that the correct object has been created.
        new_post = Post.objects.get(id=1)
        self.assertEqual(new_post.title, 'portobello')


class TestDelete_Post_view_POST(TestCase):
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