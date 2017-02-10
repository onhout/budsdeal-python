from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup', views.signup, name='user_signup'),
    url(r'^login', views.login, name='user_login'),
    url(r'^logout', views.logout, name='user_logout'),
    url(r'^home', views.home, name='user_home'),
    url(r'^settings/$', views.account_settings, name='user_settings'),
    url(r'^settings/edit_password/$', views.account_settings_password, name='user_settings_password'),

]
