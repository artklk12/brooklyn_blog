from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from hitcount.models import HitCount


class App(models.Model):
    """Приложение, одна из двух основных моделей проекта"""

    title = models.CharField(max_length=100, verbose_name='application title')
    background_img_url = models.CharField(max_length=200, blank=True, verbose_name='background image for app card')
    logo_url = models.CharField(max_length=200, blank=True, verbose_name='app logo url for app card')
    slug = models.CharField(max_length=100, verbose_name='slug in url route')
    short_desc = models.TextField(default='Нет описания', blank=True, verbose_name='short app description for app card')
    text = models.TextField(default=None, verbose_name='full app description')
    img1_url = models.CharField(max_length=200, blank=True, verbose_name='image for carousel on app page')
    img2_url = models.CharField(max_length=200, blank=True, verbose_name='image for carousel on app page')
    img3_url = models.CharField(max_length=200, blank=True, verbose_name='image for carousel on app page')
    link1 = models.CharField(max_length=200, blank=True, verbose_name='optional link on app page')
    link2 = models.CharField(max_length=200, blank=True, verbose_name='optional link on app page')
    link3 = models.CharField(max_length=200, blank=True, verbose_name='optional link on app page')
    check_status_url = models.CharField(max_length=200, blank=True, verbose_name='link to check if app is active')
    is_active = models.BooleanField(default=False, verbose_name='app is active')
    app_url = models.CharField(max_length=200, blank=True, verbose_name='application url name')
    views = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    @property
    def views_count(self):
        """Свойство для вывода количества просмотров на странице"""

        return sum([views.hits for views in self.views.all()])

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'
        ordering = ['-views__hits']


class Changelog(models.Model):
    """Описание изменений и обновлений Приложения, еще не реализованная модель в приложении"""

    app = models.ForeignKey('App', on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    changes = models.CharField(max_length=300)


class Tag(models.Model):
    """Тэг, позволяет фильтровать Посты по определенным тэгам, связь Многие-ко-Многим с Постами"""

    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, blank=True, verbose_name='slug in url route')

    def __str__(self):
        return self.title


class Post(models.Model):
    """Пост, одна из двух основных моделей приложения"""

    title = models.CharField(max_length=100, verbose_name='post title')
    author = models.CharField(max_length=100, verbose_name='post author')
    img_url = models.CharField(max_length=200, blank=True, verbose_name='post card image url')
    short_desc = models.TextField(default=None, verbose_name='short description for post card')
    text = models.TextField(default=None, verbose_name='post text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="create date")
    tags = models.ManyToManyField('Tag', related_name="posts", blank=True, verbose_name='related post tags')
    views = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    section = models.ForeignKey('Section', on_delete=models.CASCADE, verbose_name='related post section')

    def __str__(self):
        return self.title

    @property
    def views_count(self):
        """Свойство для вывода количества просмотров на странице"""

        return sum([views.hits for views in self.views.all()])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-pk']


class Comment(models.Model):
    """Комментарий, будут оставлять пользователи под Постами, еще не реализованная модель в приложении"""

    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=None, verbose_name='related post')
    author = models.CharField(max_length=100, verbose_name='comment author')
    text = models.TextField(default=None, verbose_name='comment text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="create date")


class Section(models.Model):
    """
    Раздел, в котором будут выводиться Посты(например, 'Мой блог' или 'Все статьи'), в отличие от Тэгов,
    Посты могут иметь только один раздел
    """

    title = models.CharField(max_length=100, unique=True, verbose_name='section title')

    def __str__(self):
        return self.title
