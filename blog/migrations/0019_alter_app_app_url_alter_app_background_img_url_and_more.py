# Generated by Django 4.1.7 on 2023-05-03 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0018_post_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='app_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='application url name'),
        ),
        migrations.AlterField(
            model_name='app',
            name='background_img_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='background image for app card'),
        ),
        migrations.AlterField(
            model_name='app',
            name='check_status_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='link to check if app is active'),
        ),
        migrations.AlterField(
            model_name='app',
            name='img1_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='image for carousel on app page'),
        ),
        migrations.AlterField(
            model_name='app',
            name='img2_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='image for carousel on app page'),
        ),
        migrations.AlterField(
            model_name='app',
            name='img3_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='image for carousel on app page'),
        ),
        migrations.AlterField(
            model_name='app',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='app is active'),
        ),
        migrations.AlterField(
            model_name='app',
            name='link1',
            field=models.CharField(blank=True, max_length=200, verbose_name='optional link on app page'),
        ),
        migrations.AlterField(
            model_name='app',
            name='link2',
            field=models.CharField(blank=True, max_length=200, verbose_name='optional link on app page'),
        ),
        migrations.AlterField(
            model_name='app',
            name='link3',
            field=models.CharField(blank=True, max_length=200, verbose_name='optional link on app page'),
        ),
        migrations.AlterField(
            model_name='app',
            name='logo_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='app logo url for app card'),
        ),
        migrations.AlterField(
            model_name='app',
            name='short_desc',
            field=models.TextField(blank=True, default='Нет описания', verbose_name='short app description for app card'),
        ),
        migrations.AlterField(
            model_name='app',
            name='slug',
            field=models.CharField(max_length=100, verbose_name='slug in url route'),
        ),
        migrations.AlterField(
            model_name='app',
            name='text',
            field=models.TextField(default=None, verbose_name='full app description'),
        ),
        migrations.AlterField(
            model_name='app',
            name='title',
            field=models.CharField(max_length=100, verbose_name='application title'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='related post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=None, verbose_name='comment text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100, verbose_name='post author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='post card image url'),
        ),
        migrations.AlterField(
            model_name='post',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.section', verbose_name='related post section'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_desc',
            field=models.TextField(default=None, verbose_name='short description for post card'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.tag', verbose_name='related post tags'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default=None, verbose_name='post text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='post title'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='section title'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(blank=True, max_length=50, verbose_name='slug in url route'),
        ),
    ]
