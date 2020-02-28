from django.shortcuts import render
from .models import Post


def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'forum/index.html', context)