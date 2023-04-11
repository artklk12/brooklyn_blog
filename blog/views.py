from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from .models import Post, App
from django.contrib.auth import login, logout
from .services import get_index_data, base_view, SectionListMixin, AppsListMixin, BaseView, PostDetailMixin, AppDetailMixin, TagListMixin
from django.views.generic import ListView
import logging
from hitcount.views import HitCountDetailView


logger = logging.getLogger(__name__)


@base_view
def start(request):
    apps, posts = get_index_data()
    return render(request, 'index.html', {'posts': posts, 'apps': apps})


@base_view
def blog(request):
    return redirect('blog_section', section='all')


class BlogListView(BaseView, SectionListMixin, ListView):
    paginate_by = 10
    model = Post
    template_name = "blog.html"
    allow_empty = False


class ApplicationsListView(BaseView, AppsListMixin, ListView):
    model = App
    template_name = "applications.html"
    allow_empty = False


class TagListView(BaseView, TagListMixin, ListView):
    paginate_by = 10
    model = Post
    template_name = "blog.html"
    allow_empty = False


class PostDetailView(BaseView, PostDetailMixin, HitCountDetailView):
    model = Post
    template_name = "post.html"
    count_hit = True
    allow_empty = False


class AppDetailView(BaseView, AppDetailMixin, HitCountDetailView):
    model = App
    template_name = "app.html"
    count_hit = True
    allow_empty = False


@base_view
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


@base_view
def user_logout(request):
    logout(request)
    return redirect('start')


@base_view
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
