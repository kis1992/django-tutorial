from django import template
from django.template.loader import get_template
from django.db.models import Count

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    return Post.objects.all().count()

@register.inclusion_tag('latest_post.html')
def show_latest_posts(count=2):
    latest_posts = Post.objects.all().order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=2):
    return Post.objects.all().annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
