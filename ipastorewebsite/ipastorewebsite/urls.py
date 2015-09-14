"""ipastorewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import os

ROOT_PATH = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(ROOT_PATH, '../static')

urlpatterns = [
    # ipastoreweb url patterns
    url(r'^ipa-store/$', 'ipastoreweb.views.index', name='index'),
    url(r'^ipa-store/(?P<ipa_id>[0-9]+)/$', 'ipastoreweb.views.detail',
        name='detail'),
    url(r'^ipa-store/(?P<ipa_id>[0-9]+)/download/$',
        'ipastoreweb.views.download',
        name='download'),
    url(r'^ipa-store/(?P<ipa_id>[0-9]+)/delete/$',
        'ipastoreweb.views.delete',
        name='delete'),
    url(r'^ipa-store/new/$', 'ipastoreweb.views.upload', name='upload'),

    # admin url patterns
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': STATIC_ROOT}),
]
