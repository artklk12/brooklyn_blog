from django.urls import path

from .views import start, app, apps, user_login, user_logout, register, post, BlogView

urlpatterns = [
    path('', start, name='start'),
    path('apps/', apps, name='apps'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('post/<int:pk>/', post, name='post'),
    path('app/<slug:slug>/', app, name='app'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
