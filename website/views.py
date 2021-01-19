from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from .forms import CommentForm
from django.template.defaultfilters import slugify
from taggit.models import Tag


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {'posts': posts,
               'categories': categories,
               'tags': tags}
    return render(request, 'website/home.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = post.category.all()
    comments = post.comments.all()
    new_comment = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            # new_comment.active = True
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    context = {'post': post,
               'categories': categories,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form,
               }
    return render(request, 'website/post_detail.html', context=context)


def post_by_category(request, category):
    posts = Post.objects.filter(category__topic__contains=category).order_by('-date')

    context = {'category': category, 'posts': posts}
    return render(request, 'website/post_by_category.html', context)


def post_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)
    context = {'tag': tag, 'posts': posts}
    return render(request, 'website/post_tag.html', context)


def search_result(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    context = {'posts': posts}
    return render(request, 'website/search_result.html', context)