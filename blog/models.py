from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=200, blank=True)
    img1_url = models.CharField(max_length=200, blank=True)
    img2_url = models.CharField(max_length=200, blank=True)
    img3_url = models.CharField(max_length=200, blank=True)
    text = models.TextField(default=None)
    link1 = models.CharField(max_length=200, blank=True)
    link2 = models.CharField(max_length=200, blank=True)
    link3 = models.CharField(max_length=200, blank=True)
    views_count = models.CharField(max_length=50, default=7)
    app_url = models.CharField(max_length=200, blank=True)

    # def get_absolute_url(self):
    #     return reverse_lazy('view_tasks', kwargs={"category_id": self.category.id, "pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'


class Changelog(models.Model):
    app = models.ForeignKey('App', on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    changes = models.CharField(max_length=300)


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

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

    # def get_absolute_url(self):
    #     return reverse_lazy('view_tasks', kwargs={"category_id": self.category.id, "pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=None)
    author = models.CharField(max_length=100)
    text = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")


