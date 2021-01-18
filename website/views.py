from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import CommentForm


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {'posts': posts,
               'categories': categories}
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