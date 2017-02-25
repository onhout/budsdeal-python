from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sent/$', views.view_sent_messages, name='view_sent_messages'),
    url(r'^inbox/$', views.view_inbox_messages, name='view_inbox_messages'),
    url(r'^send/(?P<social_id>[\w-]+)$', views.send_message, name='send_message'),
]
