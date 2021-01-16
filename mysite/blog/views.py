from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'blog/index.html', context)


# def post_detail(request, id):
#     post = get_object_or_404(Post, pk=id)

#     context = {'post': post}

#     return render(request, 'blog/post_detail.html', context)


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                             created__year=year,
                             created__month=month,
                             created__day=day)

    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)
