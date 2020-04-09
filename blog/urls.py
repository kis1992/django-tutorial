from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(), name = 'post_list'),
    path('share/<int:post_id>/',views.post_share, name = 'post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name = 'post_detail'),
]
