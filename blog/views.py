from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-publish')
    print(posts)
    return render(request, 'post/list.html',{'posts': posts})
# Create your views here.

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug = post, publish__year=year, publish__month=month,publish__day = day)
    return render(request, 'post/detail.html',{'post':post})
