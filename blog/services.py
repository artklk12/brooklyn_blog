# import requests
from .models import App, Post
from django.shortcuts import get_object_or_404

# def apps_is_active():
#     apps = App.objects.all()
#     for app in apps:
#         r = requests.get(url=app.check_status_url)
#         if r.ok:
#             app.is_active = True
#             app.save()
#         else:
#             app.is_active = False
#             app.save()
#     return
#


def get_index_data():
    apps = App.objects.order_by('-views_count')[0:3]
    posts = Post.objects.all()[0:2]
    return apps, posts


def get_all_apps():
    apps = App.objects.order_by('-views_count')
    return apps


def get_post(pk):
    post = get_object_or_404(Post, pk=pk)
    post.add_view()
    return post


def get_app(slug):
    app = get_object_or_404(App, slug=slug)
    app.add_view()
    return app
