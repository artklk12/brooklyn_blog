from django.urls import path, include
from django.conf import settings
from .views import start, user_login, user_logout, register, BlogListView, ApplicationsListView, PostDetailView, \
    AppDetailView

urlpatterns = [
    path('', start, name='start'),
    path('apps/', ApplicationsListView.as_view(), name='apps'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('app/<slug:slug>/', AppDetailView.as_view(), name='app'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
