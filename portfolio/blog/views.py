from django.shortcuts import render

# Create your views here.

def blog(request):
    render(request, 'blog.html')

def posts(request):
    render(request, 'posts.html')

def post_detail(request):
    render(request, 'post-details.html')
