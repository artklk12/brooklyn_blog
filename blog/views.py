from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from .services import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

def start(request):
    # apps_is_active()
    apps = App.objects.order_by('-views_count')[0:3]
    posts = Post.objects.order_by("-pk")[0:2]
    return render(request, 'index.html', {'posts': posts, 'apps': apps})

def apps(request):
    apps = App.objects.order_by('-views_count')
    return render(request, 'applications.html', {'apps': apps})


class BlogView(ListView):
    paginate_by = 2
    model = Post
    template_name = "blog.html"
    context_object_name = 'posts'

    def get_queryset(self):
        tag = self.request.GET.getlist('tag')
        if tag:
            queryset = Post.objects.filter(tags__slug__in=tag).order_by("-pk")
        else:
            queryset = Post.objects.order_by("-pk")
        return queryset


def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def app(request, slug):
    app = App.objects.get(slug=slug)
    return render(request, 'app.html', {'app': app})


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


def user_logout(request):
    logout(request)
    return redirect('start')

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