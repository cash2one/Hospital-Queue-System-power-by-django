from django.conf.urls import url
from userena import views as userena_views
from accounts.forms import *

urlpatterns = (
url(r'^signup1/$',
 'userena.views.signup',
 {'signup_form': SignupFormExtra}),
)