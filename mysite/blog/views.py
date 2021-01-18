from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from datetime import date

# Create your views here.

def index(request):
    posts = Post.objects.all()

    enumerated_posts = enumerate(posts)

    context = {'posts': enumerated_posts}

    return render(request, 'blog/index.html', context)


def posts_archive(request):

    months = Post.objects.dates('created', 'month', order='DESC')
    posts = []
    archive = {}

    for m in months:
        date = m.strftime("%B") + ' ' + str(m.year)
        for p in Post.objects.all():
            if p.created.date().month == m.month and p.created.date().year == m.year:
                posts.append(p)
        archive[date] = posts
        posts = []
    print(archive)  
        
    context = {'archive': archive}
    
    return render(request, 'blog/archive.html', context)


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                             created__year=year,
                             created__month=month,
                             created__day=day)

    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)

def menu(request):
    return render(request, 'blog/menu.html')
