from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
# from django.urls import reverse_lazy
from hitcount.models import HitCount


# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=100)
    background_img_url = models.CharField(max_length=200, blank=True)
    logo_url = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=100)
    short_desc = models.TextField(default='Нет описания', blank=True)
    text = models.TextField(default=None)
    img1_url = models.CharField(max_length=200, blank=True)
    img2_url = models.CharField(max_length=200, blank=True)
    img3_url = models.CharField(max_length=200, blank=True)
    link1 = models.CharField(max_length=200, blank=True)
    link2 = models.CharField(max_length=200, blank=True)
    link3 = models.CharField(max_length=200, blank=True)
    check_status_url = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=False)
    app_url = models.CharField(max_length=200, blank=True)
    views = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    # def get_absolute_url(self):
    #     return reverse_lazy('view_tasks', kwargs={"category_id": self.category.id, "pk": self.pk})

    def __str__(self):
        return self.title

    @property
    def views_count(self):
        """Подсчет просмотров"""
        return sum([views.hits for views in self.views.all()])

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'
        ordering = ['-views__hits']


class Changelog(models.Model):
    app = models.ForeignKey('App', on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    changes = models.CharField(max_length=300)


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    img_url = models.CharField(max_length=200, blank=True)
    short_desc = models.TextField(default=None)
    text = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    tags = models.ManyToManyField('Tag', related_name="posts", blank=True)
    views = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    section = models.ForeignKey('Section', on_delete=models.CASCADE, default=1)

    # def get_absolute_url(self):
    #     return reverse_lazy('view_tasks', kwargs={"category_id": self.category.id, "pk": self.pk})

    def __str__(self):
        return self.title

    @property
    def views_count(self):
        """Подсчет просмотров"""
        return sum([views.hits for views in self.views.all()])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-pk']


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=None)
    author = models.CharField(max_length=100)
    text = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")


class Section(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
