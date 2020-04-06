from django.urls import path
from forum import views


app_name = 'forum'
urlpatterns = [
    # Main page with all posts.
    path('', views.posts_list, name="posts_list"),
    # Post detail.
    path('<int:post_id>/<slug:post_slug>', views.post_detail, name="post_detail"),
    # Form to add new post.
    path('new_post/', views.new_post, name="new_post"),
    # Delete post.
    path('<int:post_id>/<slug:post_slug>/delete/', views.delete_post, name="delete_post"),
    # Reply.
    path('<int:post_id>/<slug:post_slug>/reply/', views.reply, name="reply"),
]