from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.list_orders, name='list_orders'),
    url(r'^create/(?P<item_id>[\w-]+)$', views.create_order, name='create_order'),
    url(r'^view/(?P<order_id>[\w-]+)$', views.view_order, name='view_order'),
    url(r'^update$', views.update_or_create, name='update_or_create_order'),
    # url(r'^details/(?P<message_id>[\w-]+)$', views.message_details, name='message_details'),
    # url(r'^delete/(?P<message_id>[\w-]+)$', views.delete_message, name='delete_message'),
]
