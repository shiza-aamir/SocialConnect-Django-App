# users/views.py (REPLACE ENTIRE FILE)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to SocialConnect!')
            return redirect('feed')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('feed')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('feed')

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    from social.models import Post
    posts = Post.objects.filter(author=user).order_by('-created_at')
    
    return render(request, 'users/profile.html', {
        'profile_user': user,
        'posts': posts,
    })

@login_required
def edit_profile(request):
    profile = request.user.profile
    
    if request.method == 'POST':
        profile.bio = request.POST.get('bio', '')
        profile.location = request.POST.get('location', '')
        
        if request.FILES.get('profile_picture'):
            profile.profile_picture = request.FILES['profile_picture']
        
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile', username=request.user.username)
    
    return render(request, 'users/edit_profile.html')