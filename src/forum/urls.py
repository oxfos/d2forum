from django.urls import path
from . import views


app_name = 'forum'
urlpatterns = [
    # Main page with all posts.
    path('', views.posts_list, name="posts_list"),
    # Post detail.
    path('<int:post_id>/<slug:post_slug>', views.post_detail, name="post_detail"),
]


