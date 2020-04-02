from django.shortcuts import render, redirect
from django.http import Http404
from .models import Post
from .forms import PostForm


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

def new_post(request):
    """Processes the form to add a new post."""
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum:posts_list')
    else:
        form = PostForm()
    return render(request, 'forum/new_post.html', {'form': form})

def delete_post(request, post_slug, post_id):
    """Deletes an existing post"""
    # We make sure it is a POST request.
    if request.method == 'POST':
        if request.POST.get('delete'):
            try:
                my_post = Post.objects.get(id=post_id)
            except:
                pass
            else:            
                if my_post.post_set.count() == 0:
                    my_post.delete()
                    return redirect('forum:posts_list')
        if request.POST.get('react'):
            return redirect('forum:posts_list')
    raise Http404