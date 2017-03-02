from django.views.generic import ListView
from django.shortcuts import render

from apps.products import models
from apps.user_messages.models import Conversations


# Create your views here.


class Index(ListView):
    model = models.Item
    template_name = 'index.html'
    context_object_name = 'product_list'
    queryset = models.Item.objects.all()

    # def get_context_data(self, **kwargs):
    #     if self.request.user.is_authenticated:
    #         context = super(Index, self).get_context_data(**kwargs)
    #         context['unread_messages'] = Conversations.objects.filter(to_user_id=self.request.user, read=False)
    #         return context


