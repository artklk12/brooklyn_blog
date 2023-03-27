from django.urls import path

from .views import *

urlpatterns = [
    path('', start, name='start'),
    path('apps/', apps, name='apps'),
    path('blog/', blog, name='blog'),
    path('post/<int:pk>/', post, name='post'),
    path('app/<slug:slug>/', app, name='app'),
    path('sidebar/', sidebar, name='sidebar'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
]