from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloworld_view(request):
    return HttpResponse('<h1>This is response from django app</h1>')
