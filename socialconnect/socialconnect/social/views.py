# social/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Like

@login_required
def feed(request):
    # For now, show all posts. Later we'll filter by followed users
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'social/feed.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        if content:
            post = Post.objects.create(author=request.user, content=content, image=image)
            messages.success(request, 'Post created successfully!')
            return redirect('feed')
        else:
            messages.error(request, 'Post content cannot be empty.')
    
    return render(request, 'social/create_post.html')

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'social/post_detail.html', {'post': post})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
            messages.success(request, 'Comment added!')
        else:
            messages.error(request, 'Comment cannot be empty.')
    
    return redirect('post_detail', post_id=post_id)

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    
    if not created:
        like.delete()
        messages.info(request, 'Post unliked!')
    else:
        messages.success(request, 'Post liked!')
    
    return redirect('feed')