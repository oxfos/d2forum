from django.urls import path
from django.http import HttpResponse

def i_am_the_view(request):
    return HttpResponse('<p>prova2</p>')

app_name = 'forum'
urlpatterns = [
    path('', i_am_the_view)
]


