from django.forms import ModelForm
from .models import Post

class PostModel(ModelForm):
    """Form to create a new post."""
    class Meta:
        model = Post