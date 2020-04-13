from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
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
    return render(request, 'forum/new_post_form.html', {'form': form})

def delete_post(request, post_slug, post_id):
    """Deletes an existing post"""
    # We make sure it is a POST request.
    # I removed the 'delete' check.
    if request.method == 'POST': 
        try:
            my_post = Post.objects.get(id=post_id)
        except:
            raise Http404
        else:            
            if my_post.post_set.count() == 0:
                my_post.delete()
                return redirect('forum:posts_list')
    raise Http404

def reply(request, post_slug, post_id):
    # View function to add reply to an existing post.
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        # If request is POST we check if the form is valid.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.ref_post = post
            new_reply.save()
            return HttpResponse('')
    elif request.method == 'GET':
        # If the form is GET we return the empty post form.
        form = PostForm()
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'partials/partial_reply_form.html', context)