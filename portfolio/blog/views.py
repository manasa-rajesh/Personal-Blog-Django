from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, 'blog/blog.html')

def posts(request):
    return render(request, 'blog/posts.html')

def post_detail(request, slug):
    return render(request, 'blog/post-details.html')
