from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/', views.add_product, name='add_product'),
    url(r'^list/', views.list_product, name='list_product'),
    url(r'^update/(?P<product_id>[\w-]+)/', views.update_product, name='update_product'),
]
