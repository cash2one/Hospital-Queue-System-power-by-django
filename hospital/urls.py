from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<id>\d+)/$', views.read_post, name='detail'),
    url(r'^about$', views.about, name='about'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.doctor_home, name='doctor_home'),
    url(r'^logout/$', views.logout_view, name='doctor_home'),
]