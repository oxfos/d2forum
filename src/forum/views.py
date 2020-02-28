from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'forum/posts_list.html', context)