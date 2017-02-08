from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^signup', views.signup, name='user_signup'),
    url(r'^login', views.login, name='user_login'),
    url(r'^logout', views.logout, name='user_logout'),
    url(r'^home', views.home, name='user_home'),
]
