from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('posts', views.posts, name="posts"),
    path('posts/<slug>', views.post_detail, name="post-details")
]