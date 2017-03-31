from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup', views.signup, name='user_signup'),
    url(r'^login', views.login, name='user_login'),
    url(r'^logout', views.logout, name='user_logout'),
    url(r'^home', views.home, name='user_home'),
    url(r'^settings/$', views.user_profile, name='user_profile'),
    url(r'^settings/company/$', views.user_company, name='user_company'),
    url(r'^settings/save/$', views.save_account_settings, name='save_settings'),
    url(r'^settings/company/save/$', views.save_company_info, name='save_company_info'),
    url(r'^settings/edit_password/$', views.account_settings_password, name='user_settings_password'),
    url(r'^view/(?P<display_name>[\w-]+)', views.view_profile, name='view_profile'),
    url(r'^seller/register', views.register_as_seller, name='register_as_seller'),
    url(r'^feedback/post/(?P<display_name>[\w-]+)', views.post_user_feedback, name='user_feedback'),
]
