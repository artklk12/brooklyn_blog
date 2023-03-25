from django.urls import path

from .views import *

urlpatterns = [
    path('', start, name='start'),
    path('apps/', apps, name='apps'),
    path('blog/', blog, name='blog'),
    path('post/<int:pk>/', post, name='post'),
    path('sidebar/', sidebar, name='sidebar'),


]