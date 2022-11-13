from unicodedata import category
from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    featured_post = Post.objects.all().filter(category=0)[:1]
    django_post = Post.objects.all().filter(fram=0)[:2]
    flask_post = Post.objects.all().filter(fram=1)[:2]

    context = {'featured_post':featured_post,'django_post':django_post,'flask_post':flask_post}
    return render(request, 'core/index.html', context)



def PostDetail(request,pk):
    post_detail = Post.objects.filter(pk=pk)
    context = {'post_detail':post_detail}
    return render(request, 'core/post_detail.html', context)
