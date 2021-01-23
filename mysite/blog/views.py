from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Q
from .models import Post
from datetime import date


# Create your views here.

def index(request):
    
    posts = Post.objects.all()

    context = {'posts': posts}
    
    return render(request, 'blog/index.html', context)


def posts_archive(request):

    ######################################

    meses = {
            'January': 'Enero',
            'February': 'Febrero',
            'March': 'Marzo',
            'April': 'Abril',
            'May': 'Mayo',
            'June': 'Junio',
            'July': 'Julio',
            'August': 'Agosto',
            'September': 'Septiembre',
            'October': 'Octubre',
            'November': 'Noviembre',
            'December': 'Diciembre'    
            }

    #######################################

    context = {}

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    def get_posts_by_content_queryset(query=None):
        return Post.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(created__icontains=query)
        ).distinct()


    ####################################################


    months = get_posts_by_content_queryset(query).dates('created', 'month', order='DESC')

    # months = Post.objects.dates('created', 'month', order='DESC')
    posts = []
    archive = {}


    for m in months:
        date = meses[m.strftime("%B")] + ' ' + str(m.year)
        # for p in Post.objects.all():
        for p in get_posts_by_content_queryset(query):
            if p.created.date().month == m.month and p.created.date().year == m.year:
                posts.append(p)
        archive[date] = posts
        posts = []
        
    context['archive'] = archive
    
    return render(request, 'blog/archive.html', context)


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                             created__year=year,
                             created__month=month,
                             created__day=day)

    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)


def about(request):
    try:
        p = Post.objects.get(pk=1000)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'about.html', {'post': p})


def error_404_view(request, exception):
    return render(request, '404.html')

