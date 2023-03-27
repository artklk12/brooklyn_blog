from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout



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


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('start')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('start')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})