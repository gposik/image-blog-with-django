from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('archive/', views.posts_archive, name='archive'),
    path('menu/', views.menu, name='menu'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail,
         name='post_detail')
]

urlpatterns += staticfiles_urlpatterns()
