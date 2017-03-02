from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/', views.add_product, name='add_product'),
    url(r'^list/', views.list_product, name='list_product'),
    url(r'^update/(?P<product_id>[\w-]+)/', views.update_product, name='update_product'),
    url(r'^delete/(?P<product_id>[\w-]+)/', views.delete_product, name='delete_product'),
    url(r'^view/(?P<product_id>[\w-]+)/', views.view_product, name='view_product'),
    url(r'^category/(?P<category_slug>[\w-]+)/(?P<subcategory_slug>[\w-]+)/', views.list_categories, name='view_product'),
]
