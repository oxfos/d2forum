from django.urls import path
from . import views


app_name = 'forum'
urlpatterns = [
    path('', views.posts_list, name="posts_list"),
    path('<slug:post_slug>/<int:post_id>', views.post_detail, name="post_detail"),
]


