from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

class PostListView(ListView):
    queryset = Post.objects.order_by('-publish')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post/list.html'

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
