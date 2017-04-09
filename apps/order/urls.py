from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.list_orders, name='list_orders'),
    # url(r'^inbox/$', views.view_inbox_messages, name='view_inbox_messages'),
    # url(r'^send/(?P<social_id>[\w-]+)/item/(?P<item_id>[\w-]+)$', views.send_message, name='send_message'),
    # url(r'^details/(?P<message_id>[\w-]+)$', views.message_details, name='message_details'),
    # url(r'^delete/(?P<message_id>[\w-]+)$', views.delete_message, name='delete_message'),
]
