from django.shortcuts import render, get_object_or_404

from .models import Author, BlogPost


def index(request):
    posts = BlogPost.objects.all()
    context = {
        'title': 'Blogs',
        'posts': posts
    }
    return render(request, 'blog/index.html', context=context)


def detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'title': 'Detail',
        'post': post
    }
    return render(request, 'blog/detail.html', context=context)