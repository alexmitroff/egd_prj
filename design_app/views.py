from django.shortcuts import render
from egd_prj import settings
from django.http import JsonResponse

from design_app.models import *
import json



# Create your views here.

def index(request):
    template = 'pages/index.html'
    var = {}
    return render(request, template, var)

def news(request):
    template = 'pages/news.html'
    var = {}
    return render(request, template, var)

def feed(request):
    l = request.LANGUAGE_CODE
    if 'category' in request.GET:
        news = NewsItem.objects.filter(publish=True, 
                category=request.GET['category'])
    else:
        news = NewsItem.objects.filter(publish=True)

    if l == 'ru':
        data = [{'date':item.created,'color':item.category.color,
            'category':item.category.name_ru,'title': item.title_ru, 
            'short': item.content_ru} for item in news]
    else:
        data = [{'date':item.created,'color':item.category.color,
            'category':item.category.name_en,'title': item.title_en, 
            'short': item.content_en} for item in news]

    return JsonResponse(data, safe=False)
