# Generated by Django 4.1.7 on 2023-03-25 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_changelog_comment_tag_rename_github_url_app_img1_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='app_url',
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
    ]
