from django.shortcuts import render
from .models import *

def start(request):
    posts = Post.objects.order_by("-pk")[0:2]
    return render(request, 'index.html', {'posts': posts})

def apps(request):
    apps = App.objects.order_by('views_count')
    return render(request, 'applications.html', {'apps': apps})

def blog(request):
    posts = Post.objects.order_by("-pk")
    return render(request, 'blog.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def app(request, slug):
    app = App.objects.get(slug=slug)
    return render(request, 'app.html', {'app': app})

def sidebar(request):
    return render(request, 'sidebar.html')