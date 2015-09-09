__author__ = 'mertsalik'

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('views',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<ipa_id>[0-9]+)/$', views.detail,
                           name='detail'),
                       url(r'^(?P<ipa_id>[0-9]+)/download/$', views.download,
                           name='download'),
                       )
