from django.conf.urls import patterns, include, url
from django.contrib import admin
from machina.app import board
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('hospital.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^markdown/', include( 'django_markdown.urls')),
    url(r'^forum/', include(board.urls)),
    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
)
