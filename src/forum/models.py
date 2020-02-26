from django.db import models

class Post(models.Model):
    """A Post the user posts on the forum."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a sting representation of the model."""
        return self.title