from django.shortcuts import render

def start(request):
    return render(request, 'index.html')

def apps(request):
    return render(request, 'apps.html')

def blog(request):
    return render(request, 'blog.html')

def post(request, pk):
    return render(request, 'post.html')

def sidebar(request):
    return render(request, 'sidebar.html')