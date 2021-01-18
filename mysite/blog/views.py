from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'blog/index.html', context)


def posts_archive(request):

    def group_by_date():
        index = 0
        actual_post = Post.objects.all()[index]

        year = actual_post.created.year
        month = actual_post.created.month

        years = {}
        months = {}
        posts = []

        print(year)
        while (year == actual_post.created.year):
            print(month)
            while (year == actual_post.created.year and month == actual_post.created.month):
                posts.append(actual_post)
                print(actual_post.title)
                index+= 1
                if index < Post.objects.count():
                    actual_post = Post.objects.all()[index]
                else:
                    months[month] = posts
                    years[year] = months
                    return years
            months[month] = posts
            month = actual_post.created.month
        years[year] = months
        year = actual_post.created.year
        
        return years

    context = {'posts': group_by_date()}

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