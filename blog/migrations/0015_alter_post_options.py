# Generated by Django 4.1.7 on 2023-04-05 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_app_views_count_remove_post_views_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]