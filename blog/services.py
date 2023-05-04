from django.db import transaction
from django.urls import reverse
from .models import App, Post
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseServerError
from django.views import generic, View
from .forms import CommentForm
import logging
import functools


logger = logging.getLogger(__name__)


class BaseView(View):
    """Базовый класс для всех view, добавляет логирование и обработку исключений"""

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
    """Базовый декоратор для всех view, добавляет логирование и обработку исключений"""

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


class TagListMixin(generic.base.ContextMixin):
    """Миксин для возвращения queryset, с Постами, у которых есть определенный Тэг"""

    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(tags__slug=self.kwargs['tag']).prefetch_related('views', 'tags')
        return queryset


class SectionListMixin(generic.base.ContextMixin):
    """Миксин для возвращения queryset, с Постами, которые принадлежат к определенной категории"""

    context_object_name = 'posts'

    def get_queryset(self):
        section = self.kwargs['section']
        if section == 'all':
            queryset = Post.objects.prefetch_related('views', 'tags')
        else:
            queryset = Post.objects.filter(section__title=section).prefetch_related('views', 'tags')
        return queryset


class AppDetailMixin(generic.base.ContextMixin):
    """Миксин для возвращения Приложения или Http404"""

    def get_object(self):
        obj = get_object_or_404(App.objects.prefetch_related('views'), slug=self.kwargs['slug'])
        return obj


class PostDetailMixin(generic.base.ContextMixin):
    """Миксин для возвращения Поста или Http404"""

    def get_object(self):
        obj = get_object_or_404(Post.objects.prefetch_related('views', 'tags', 'comments__author'), pk=self.kwargs['pk'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentMixin(generic.edit.FormMixin):

    def get_success_url(self):
        return reverse('post', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


def get_index_data():
    """Функция для получения Постов и Приложений для главной страницы"""

    apps = App.objects.prefetch_related('views')[0:3]
    posts = Post.objects.prefetch_related('views', 'tags')[0:2]
    return apps, posts
