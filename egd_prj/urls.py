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

ru_flat = [
    url(r'contacts/$', fp_views.flatpage, {'url': '/ru/contacts/'}, name='contacts_ru'),
    url(r'about/$', fp_views.flatpage, {'url': '/ru/about/'}, name='about_ru'),
    url(r'ecodesign/$', fp_views.flatpage, {'url': '/ru/ecodesign/'}, name='ecodesign_ru'),
    url(r'international/$', fp_views.flatpage, {'url': '/ru/international/'}, name='international_ru'),
    url(r'scientific/$', fp_views.flatpage, {'url': '/ru/scientific/'}, name='scientific_ru'),
    url(r'laboratories/$', fp_views.flatpage, {'url': '/ru/laboratories/'}, name='laboratories_ru'),
    url(r'applications/bachelor/$', fp_views.flatpage, {'url': '/ru/applications/bachelor/'}, name='app_bach_ru'),
    url(r'applications/masters/$', fp_views.flatpage, {'url': '/ru/applications/masters/'}, name='app_mast_ru'),
        ]

en_flat = [
    url(r'contacts/$', fp_views.flatpage, {'url': '/en/contacts/'}, name='contacts_en'),
    url(r'about/$', fp_views.flatpage, {'url': '/en/about/'}, name='about_en'),
    url(r'ecodesign/$', fp_views.flatpage, {'url': '/en/ecodesign/'}, name='ecodesign_en'),
    url(r'international/$', fp_views.flatpage, {'url': '/en/international/'}, name='international_en'),
    url(r'scientific/$', fp_views.flatpage, {'url': '/en/scientific/'}, name='scientific_en'),
    url(r'laboratories/$', fp_views.flatpage, {'url': '/en/laboratories/'}, name='laboratories_en'),
    url(r'applications/bachelor/$', fp_views.flatpage, {'url': '/en/applications/bachelor/'}, name='app_bach_en'),
    url(r'applications/masters/$', fp_views.flatpage, {'url': '/en/applications/masters/'}, name='app_mast_en'),
        ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^en/', include(en_flat)),
    url(r'^ru/', include(ru_flat)),
    url(r'^api/', include(api_patterns)),
]

urlpatterns += i18n_patterns(
    url(r'^$', views.news, name='news'),
    url(r'^applicants/$', views.applicants, name='applicants'),
    url(r'^applicants/(?P<d_slug>.*)/(?P<p_slug>.*)/$', views.programm, name='programm'),
    url(r'^applicants/(?P<d_slug>.*)/$', views.degree, name='degree'),
    )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
