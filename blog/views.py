from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from . forms import EmailPostForm
from django.core.mail import send_mail



class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post/list.html'

def post_share(request, post_id):
    post = get_object_or_404(Post, id = post_id, status = 'published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comment'])
            send_mail(subject, message, 'oraz.mergen@gmail.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render( request, 'post/share.html', { 'post':post, 'form':form,'sent':sent } )

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug = post, publish__year=year, publish__month=month,publish__day = day)
    return render(request, 'post/detail.html',{'post':post})
