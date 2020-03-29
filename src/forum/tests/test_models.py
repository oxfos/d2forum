from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify
from forum.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.post = Post.objects.create(title='my dummy title', text='my_text',)

    def test_post_creation(self):
        # Test post is an instance of Post.
        self.assertTrue(isinstance(self.post, Post))
        # Test title is what should be.
        self.assertEqual(self.post.title, 'my dummy title')
        # Test string representation of post.
        self.assertEqual(str(self.post),'my dummy title')
        # Test slug.
        my_slug = slugify(self.post.title)
        self.assertEqual(self.post.slug, my_slug)
    
    def test_field_labels(self):
        # Test title label.
        title_label = self.post._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')
        # Test text label.
        text_label = self.post._meta.get_field('text').verbose_name
        self.assertEqual(text_label, 'text')
        # Test date_added label.
        date_added_label = self.post._meta.get_field('date_added').verbose_name
        self.assertEqual(date_added_label, 'date added')

    def test_field_max_lengths(self):
        # Test title field max length.
        title_length = self.post._meta.get_field('title').max_length
        self.assertEqual(title_length, 200)

    def test_post_object_name(self):
        # Test that title is used as object name.
        post = self.post
        expected_object_name = self.post.title
        self.assertEqual(expected_object_name, str(post))