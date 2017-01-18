# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
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
    categories = NewsCategory.objects.all()
    var = {'categories':categories}
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

def applicants(request):
    template = 'pages/applicants.html'
    degrees = Degree.objects.filter(show=True)
    units = Unit.objects.filter(tag__word='apply')
    var = {'degrees':degrees,
           'units':units}
    return render(request, template, var)

def degree(request, d_slug):
    template = 'pages/degree.html'
    degree = get_object_or_404(Degree, slug=d_slug)
    var = {'degree':degree}
    return render(request, template, var)

def programm(request,d_slug, p_slug):
    template = 'pages/programm.html'
    degree = get_object_or_404(Degree, slug=d_slug)
    programm = get_object_or_404(Programm, slug=p_slug)
    var = { 'degree':degree,
            'programm':programm}
    return render(request, template, var)
