from django.urls import path
from .views import start, user_login, user_logout, register, BlogListView, ApplicationsListView, PostDetailView, \
    AppDetailView, TagListView, blog


urlpatterns = [
    path('', start, name='start'),
    path('apps/', ApplicationsListView.as_view(), name='apps'),
    path('blog/', blog, name='default_blog'),
    path('blog/<slug:section>/', BlogListView.as_view(), name='blog_section'),
    path('blog/tag/<slug:tag>/', TagListView.as_view(), name='blog_tag'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('app/<slug:slug>/', AppDetailView.as_view(), name='app'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
