from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {'posts': posts,
               'categories': categories}
    return render(request, 'website/home.html', context)
