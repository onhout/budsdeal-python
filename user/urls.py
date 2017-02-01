from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    url(r'^signup/', views.signup, name='user_signup'),
    url(r'^login/', views.login, name='user_login'),
    url(r'^obtain-auth-token/$', obtain_auth_token)
]
