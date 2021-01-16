from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    # path('<int:id>', views.post_detail, name='post_detail')
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail,
         name='post_detail')
]

urlpatterns += staticfiles_urlpatterns()
