from django.urls import path

from blog.views import create_blog, all_blogs

app_name = 'blog'

urlpatterns = [
    path('create_blog/', create_blog, name='create_blog'),
    path('', all_blogs, name='all_blogs'),
]