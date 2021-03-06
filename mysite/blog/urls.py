from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('archive/', views.posts_archive, name='archive'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail,
         name='post_detail'),
    path('about/', views.about, name='about'),
    path('post/add/', views.post_add, name='add'),
    path('post/update/<int:id>/', views.post_update, name='update'),
]

urlpatterns += staticfiles_urlpatterns()

handler404 = 'blog.views.error_404_view'