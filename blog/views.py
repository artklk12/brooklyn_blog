from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from .models import Post
from django.contrib.auth import login, logout
# from .services import apps_is_active
from .services import get_index_data, get_all_apps, get_post, get_app
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .mixins import BlogPostsMixin


def start(request):
    # apps_is_active()
    apps, posts = get_index_data()
    return render(request, 'index.html', {'posts': posts, 'apps': apps})


def apps(request):
    apps = get_all_apps()
    return render(request, 'applications.html', {'apps': apps})


class BlogView(BlogPostsMixin, ListView):
    paginate_by = 2
    model = Post
    template_name = "blog.html"


def post(request, pk):
    post = get_post(pk)
    return render(request, 'post.html', {'post': post})


def app(request, slug):
    app = get_app(slug)
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
