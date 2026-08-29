from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        "posts":posts,
    }
    return render(request, "blogs/index.html", context)

def about(request):
    return render(request, "blogs/about.html")
