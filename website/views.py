from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q, Count
from .forms import CommentForm
from django.template.defaultfilters import slugify
from taggit.models import Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def popular_posts():
    return Post.objects.order_by('-view_count')[:2]


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page', 1)
    post_list = paginator.page(page)
    context = {'posts': post_list,
               'categories': categories,
               'tags': tags,
               'post_list': post_list,
               'popular_posts': popular_posts()}
    return render(request, 'website/home.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.view_count += 1
    post.save()
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
               'popular_posts': popular_posts(),
               }
    return render(request, 'website/post_detail.html', context=context)


def post_by_category(request, category):
    posts = Post.objects.filter(category__topic__contains=category).order_by('-date')

    context = {'category': category,
               'posts': posts,
               'popular_posts': popular_posts()}
    return render(request, 'website/post_by_category.html', context)


def post_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)
    context = {'tag': tag,
               'posts': posts,
               'popular_posts': popular_posts()}
    return render(request, 'website/post_tag.html', context)


def search_result(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    context = {'posts': posts,
               'popular_posts': popular_posts()}
    return render(request, 'website/search_result.html', context)