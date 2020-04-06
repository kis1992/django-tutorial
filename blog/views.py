from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    object_list = Post.objects.order_by('-publish')
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    print(posts)
    return render(request, 'post/list.html',{'posts': posts})
# Create your views here.

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug = post, publish__year=year, publish__month=month,publish__day = day)
    return render(request, 'post/detail.html',{'post':post})
