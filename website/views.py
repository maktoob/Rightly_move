from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {'posts': posts,
               'categories': categories}
    return render(request, 'website/home.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = post.category.all()
    context = {'post': post,
               'categories': categories,
               }
    return render(request, 'website/post_detail.html', context=context)

