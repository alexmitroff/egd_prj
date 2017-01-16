"""
egd_prj URL Configuration

URLs includes API.
Well it is not REST, but some sort of.
It returns JSON.
"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.flatpages import views as fp_views
from design_app import views

api_patterns = [
    url(r'feed/$', views.feed, name='feed'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^api/', include(api_patterns)),
]

urlpatterns += i18n_patterns(
    url(r'^$', views.index, name='index'),
    url(r'^news/$', views.news, name='news'),
    )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
