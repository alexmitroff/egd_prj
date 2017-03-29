# -*- coding: utf-8 -*-
from django.contrib import admin
from design_app.models import *
from django.utils.translation import ugettext_lazy as _

# Register your models here.

class NewsItemAdmin(admin.ModelAdmin):
    """
    News filtered by category and publish state.

    """
    list_filter = ('category', 'publish')

class ProgrammImageInline(admin.StackedInline):
    model = ProgrammImage
    extra=0

class ProgrammAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {'fields':('pos','show','slug','degree',
                'form','duration','color','pic')}),
            (_('Russian locale'), {'fields':('name_ru','summary_ru',
                'short_ru','content_ru','courses_ru','inter_ru','tech_ru')}),
            (_('English locale'), {'fields':('name_en','summary_en',
                'short_en','content_en','courses_en','inter_en','tech_en')}),
            )
    list_filter = ('degree', 'form')
    inlines = [ ProgrammImageInline, ]

admin.site.register(Tag)
admin.site.register(Lab)
admin.site.register(FlatImage)
admin.site.register(Unit)
admin.site.register(Degree)
admin.site.register(Programm, ProgrammAdmin)
admin.site.register(NewsCategory)
admin.site.register(NewsItem, NewsItemAdmin)
