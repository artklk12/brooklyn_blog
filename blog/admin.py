from django.contrib import admin

from .models import *
# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'img_url', 'short_desc', 'text',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'title',)
    list_editable = ('text',)
    list_filter = ('tags', 'author',)
    readonly_fields = ('created_at',)
    filter_horizontal = ('tags',)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at', 'text',)
    list_display_links = ('id',)
    readonly_fields = ('created_at',)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id',)


admin.site.register(Post, PostsAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Tag, TagsAdmin)

