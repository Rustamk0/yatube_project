from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    title = 'Записи сообщества'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    group = get_object_or_404(Group, slug=slug)
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context) 