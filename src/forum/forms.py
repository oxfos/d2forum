from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    """Form to create a new post."""
    class Meta:
        model = Post
        fields = ['title', 'text']