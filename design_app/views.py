# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from egd_prj import settings
from django.http import JsonResponse

from design_app.models import *
import json



# Create your views here.

def get_news():
    return NewsItem.objects.filter(featured = True)

def index(request):
    template = 'pages/index.html'
    var = {}
    return render(request, template, var)

def news(request):
    template = 'pages/news.html'
    categories = NewsCategory.objects.all()
    carousel = get_news()
    var = {
            'categories':categories,
            'carousel':carousel,
            }
    return render(request, template, var)

def fix_date(d):
    return d.strftime('%d.%m.%Y')

def feed(request):
    l = request.LANGUAGE_CODE
    if 'category' in request.GET:
        news = NewsItem.objects.filter(publish=True, 
                category=request.GET['category'])
    else:
        news = NewsItem.objects.filter(publish=True)

    if l == 'ru':
        data = [{'date':fix_date(item.created),'color':item.category.color,
            'category':item.category.name_ru,'title': item.title_ru, 
            'short': item.content_ru} for item in news]
    else:
        data = [{'date':fix_date(item.created),'color':item.category.color,
            'category':item.category.name_en,'title': item.title_en, 
            'short': item.content_en} for item in news]

    return JsonResponse(data, safe=False)

def applicants(request):
    template = 'pages/applicants.html'
    units = Unit.objects.filter(tag__word='apply')
    var = {'units':units}
    return render(request, template, var)

def degree(request, d_slug):
    template = 'pages/degree.html'
    degree = get_object_or_404(Degree, slug=d_slug)
    programmes = Programm.objects.filter(show=True, degree=degree.id)
    form0 = programmes.filter(form=0)
    #form1 = programmes.filter(form=1)
    #form2 = programmes.filter(form=2)
    var = { 
            'degree':degree,
            'form0':form0,
            'carousel':form0,
            }
    return render(request, template, var)

def programm(request,d_slug, p_slug):
    l = request.LANGUAGE_CODE
    template = 'pages/programm.html'
    degree = get_object_or_404(Degree, slug=d_slug)
    programm = get_object_or_404(Programm, slug=p_slug)
    images = ProgrammImage.objects.filter(show=True, programm = programm.pk)[:3]
    apply_url = "/{0}/applications/{1}/".format(l,degree.slug)
    var = { 'degree':degree,
            'programm':programm,
            'apply':apply_url,
            'images':images}
    return render(request, template, var)

def labs(request):
    template = 'pages/labs.html'
    degrees = Degree.objects.filter(show=True)
    labs = Lab.objects.filter(show=True)
    var = {'labs':labs,
            'carousel':labs}
    return render(request, template, var)

def lab(request,l_slug):
    template = 'pages/lab.html'
    lab = Lab.objects.filter(slug=l_slug)
    var = {
            'lab':lab[0],
            'carousel':lab,
        }
    return render(request, template, var)
