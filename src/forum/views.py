from django.shortcuts import render
from .models import Post


def posts_list(request):
    """View to list all posts."""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'forum/posts_list.html', context)

def post_detail(request, post_slug, post_id):
    """View to display post detail."""
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'forum/post_detail.html', context)