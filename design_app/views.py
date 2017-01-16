from django.shortcuts import render
from egd_prj import settings

# Create your views here.

def index(request):
    template = 'pages/index.html'
    var = {}
    return render(request, template, var)

def news(request):
    template = 'pages/news.html'
    var = {}
    return render(request, template, var)
