from django.shortcuts import render
from django.http import HttpResponse


def i_am_the_view(request):
    return HttpResponse('<p>prova2</p>')