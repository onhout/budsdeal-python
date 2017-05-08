from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.list_orders, name='list_orders'),
    url(r'^list_seller_products/(?P<order_id>[\w-]+)$', views.list_seller_products, name='list_seller_products'),
    url(r'^item/add/(?P<order_id>[\w-]+)$', views.add_to_order, name='add_to_order'),
    url(r'^item/remove/(?P<order_id>[\w-]+)$', views.remove_from_order, name='remove_from_order'),
    url(r'^create/(?P<item_id>[\w-]+)$', views.create_order, name='create_order'),
    url(r'^view/(?P<order_id>[\w-]+)$', views.view_order, name='view_order'),
    url(r'^cancel/(?P<order_id>[\w-]+)$', views.cancel_order, name='cancel_order'),
    url(r'^update$', views.update_or_create, name='update_or_create_order'),
    url(r'^confirm/(?P<order_id>[\w-]+)$', views.confirm_order, name='confirm_order'),
    url(r'^view_all_message/(?P<order_id>[\w-]+)$', views.view_all_message, name='view_all_message'),
    # url(r'^delete/(?P<message_id>[\w-]+)$', views.delete_message, name='delete_message'),
]
