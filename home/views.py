from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
# Create your views here.

def index(request):
    msg = 'My message'
    return render(request, 'index.html', {'message' : msg})

def error(request):
    raise Http404("Not Found")