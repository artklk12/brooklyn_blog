# Generated by Django 4.1.7 on 2023-03-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_app_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='check_status_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='app',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='app',
            name='short_desc',
            field=models.TextField(blank=True, default='Нет описания'),
        ),
        migrations.AddField(
            model_name='post',
            name='views_count',
            field=models.CharField(default=7, max_length=50),
        ),
    ]
