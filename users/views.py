from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from .forms import URegister
from blogs.models import Post

def register(request):
    if request.method == 'POST':
        form = URegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')
    else:
        form = URegister()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user).order_by('-date_posted')    
    context = {
        'posts': posts
    }
    return render(request, "users/profile.html", context)
