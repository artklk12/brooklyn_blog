# import requests
from django.db import transaction
from .models import App, Post
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponseServerError
from django.views import generic, View
import logging
import functools


logger = logging.getLogger(__name__)


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


class BaseView(View):
    """ Базовый класс для всех view, добавляет логирование и обработку исключений"""

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
            return response
        except Http404 as ex:
            logger.exception(ex)
            raise Http404
        except Exception as ex:
            logger.exception(ex)
            return HttpResponseServerError('Internal Server Error')


def base_view(func):
    @functools.wraps(func)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return func(request, *args, **kwargs)
        except Http404 as ex:
            logger.exception(ex)
            raise Http404
        except Exception as ex:
            logger.exception(ex)
            return HttpResponseServerError('Internal Server Error')
    return inner


class PostsListMixin(generic.base.ContextMixin):
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = self.request.GET.get('tag')
        if self.tag:
            queryset = get_list_or_404(Post.objects.filter(tags__slug=self.tag).prefetch_related('views', 'tags'))
        else:
            queryset = get_list_or_404(Post.objects.prefetch_related('views', 'tags'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class AppsListMixin(generic.base.ContextMixin):
    context_object_name = 'apps'

    def get_queryset(self):
        queryset = get_list_or_404(App.objects.prefetch_related('views'))
        return queryset


class AppDetailMixin(generic.base.ContextMixin):

    def get_object(self):
        obj = get_object_or_404(App.objects.prefetch_related('views'), slug=self.kwargs['slug'])
        return obj


class PostDetailMixin(generic.base.ContextMixin):

    def get_object(self):
        obj = get_object_or_404(Post.objects.prefetch_related('views', 'tags'), pk=self.kwargs['pk'])
        return obj


def get_index_data():
    apps = App.objects.prefetch_related('views')[0:3]
    posts = Post.objects.prefetch_related('views', 'tags')[0:2]
    return apps, posts
