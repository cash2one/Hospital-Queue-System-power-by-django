from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<id>\d+)/$', views.read_post, name='detail'),
    url(r'^about$', views.about, name='about'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.doctor_home, name='doctor_home'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^getdoctorname/$',views.ajax_used_to_select_doctor,name='ajax_used_to_select_doctor'),
    url(r'^patient_home/$',views.patient_home,name='patient_home'),
    url(r'^detail/(?P<id>\d+)/$', views.huizhen, name='huizhen'),
    url(r'^huizheng_history/$', views.huizhen_history, name='huizhen_history'),
    url(r'^huizhen_history_detail/(?P<id>\d+)/$', views.huizhen_history_detail, name='huizhen_history_detail'),
    url(r'^huizhen_history_patient/$', views.huizhen_history_patient, name='huizhen_history_patient'),
    url(r'^huizhen_history_detail_patient/(?P<id>\d+)/$', views.huizhen_history_detail_patient, name='huizhen_history_detail_patient'),
]