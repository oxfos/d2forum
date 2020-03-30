from django.test import SimpleTestCase
from forum.forms import PostForm

class PostFormTest(SimpleTestCase):
    """Class to test the PostForm form."""
    def test_post_form_field_labels(self):
        # Test field labels.
        form = PostForm()
        self.assertEqual(form.fields['title'].label, 'Title')
        self.assertEqual(form.fields['text'].label, 'Text')

    def test_post_form_field_help_text(self):
        # Test help texts.
        form = PostForm()
        self.assertTrue(form.fields['title'].help_text == '')

    def test_post_form_invalid(self):
        # Test an invalid form.
        form = PostForm(data = {'title': 'some title'})
        self.assertFalse(form.is_valid())

    def test_post_form_valid(self):
        # Test a valid form.
        form = PostForm(data={'title': 'my title', 'text': 'my text'})
        self.assertTrue(form.is_valid())