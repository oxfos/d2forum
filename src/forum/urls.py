from django.urls import path
from . import views


app_name = 'forum'
urlpatterns = [
    path('', views.i_am_the_view, name="i_view"),
]


