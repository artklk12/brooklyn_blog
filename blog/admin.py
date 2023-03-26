from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *
# Register your models here.


class PostAdminForm(forms.ModelForm):
    short_desc = forms.CharField(widget=CKEditorUploadingWidget())
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class AppAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())


    class Meta:
        model = App
        fields = '__all__'


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'img_url', 'short_desc', 'text',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_editable = ('text', 'short_desc',)
    list_filter = ('tags', 'author',)
    readonly_fields = ('created_at',)
    filter_horizontal = ('tags',)
    form = PostAdminForm


class AppsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo_url', 'views_count',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    form = AppAdminForm


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_at', 'text',)
    list_display_links = ('id',)
    readonly_fields = ('created_at',)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id',)


admin.site.register(Post, PostsAdmin)
admin.site.register(App, AppsAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Tag, TagsAdmin)

