from django.urls import path
from . import views


app_name = 'forum'
urlpatterns = [
    path('', views.posts_list, name="posts_list"),
    path('<int:post_id>/<slug:post_slug>', views.post_detail, name="post_detail"),
]


