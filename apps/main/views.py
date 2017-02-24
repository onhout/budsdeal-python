from django.views.generic import ListView

from apps.products import models


# Create your views here.


class Index(ListView):
    model = models.Item
    template_name = 'index.html'
    context_object_name = 'product_list'
    queryset = models.Item.objects.all()
