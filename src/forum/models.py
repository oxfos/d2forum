from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    """A Post a user posts on the forum."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    ref_post = models.ForeignKey('self', null=True, on_delete=models.PROTECT)

    def __str__(self):
        """Returns a sting representation of the model."""
        return self.title

    def save(self, *args, **kwargs):
        """Automatically convert title into slug upon saving."""
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)