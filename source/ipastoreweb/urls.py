__author__ = 'mertsalik'

from django.conf.urls import patterns, url

from . import views

# urlpatterns = [
#     # ex: /ipa-store/
#     url(r'^$', views.index, name='index'),
#     # ex: /ipa-store/5/
#     url(r'^(?P<ipa_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /ipa-store/5/download/
#     url(r'^(?P<ipa_id>[0-9]+)/download/$', views.download,
#         name='download'),
# ]

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<ipa_id>[0-9]+)/$', views.detail,
                           name='detail'),
                       url(r'^(?P<ipa_id>[0-9]+)/download/$', views.download,
                           name='download'),
                       )
