from django.contrib import admin
from design_app.models import *

# Register your models here.

class NewsItemAdmin(admin.ModelAdmin):
    """
    News filtered by category and publish state.

    """
    list_filter = ('category', 'publish')

admin.site.register(NewsCategory)
admin.site.register(NewsItem, NewsItemAdmin)
