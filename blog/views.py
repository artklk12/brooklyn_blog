from django.shortcuts import render
from .models import *

def start(request):
    posts = Post.objects.order_by("-pk")[0:2]
    return render(request, 'index.html', {'posts': posts})

def apps(request):
    return render(request, 'apps.html')

def blog(request):
    posts = Post.objects.order_by("-pk")
    return render(request, 'blog.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def sidebar(request):
    return render(request, 'sidebar.html')