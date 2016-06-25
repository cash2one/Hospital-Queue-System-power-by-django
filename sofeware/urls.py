from django.conf.urls import patterns, include, url
from django.contrib import admin
from machina.app import board
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sofeware.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('hospital.urls')),
    url(r'^markdown/', include( 'django_markdown.urls')),
    url(r'^forum/', include(board.urls)),
    url(r'^accounts/', include('userena.urls')),
)
