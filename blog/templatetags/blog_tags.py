from django import template
from django.template.loader import get_template

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    return Post.objects.all().count()

t = get_template('latest_post.html')

@register.inclusion_tag(t)
def show_latest_posts(count=2):
    latest_posts = Post.objects.all().order_by('-publish')[:count]
    print('location template= ',t)
    return {'latest_posts': latest_posts}
