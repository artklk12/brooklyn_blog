from .models import Post
from django.views import generic
from django.shortcuts import get_list_or_404


class BlogPostsMixin(generic.base.ContextMixin):
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = self.request.GET.get('tag')
        if self.tag:
            queryset = get_list_or_404(Post, tags__slug=self.tag)
        else:
            queryset = Post.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
