from django.views.generic import ListView
from django.shortcuts import render
import random

from apps.products import models


# Create your views here.


class Index(ListView):
    model = models.Item
    template_name = 'index.html'
    context_object_name = 'product_list'
    queryset = models.Item.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super(Index, self).get_context_data(**kwargs)
    #     #get child category
    #     cats = models.Category.objects.filter(parent_category__isnull=False)
    #     #get random choice
    #     cat = random.choice(cats)
    #     #get total count from items from the cat choice
    #     item_num = models.Item.objects.filter(categories=cat).count()
    #     # get the list of IDs (max 5)
    #     if item_num < 5:
    #         rand_count = item_num
    #     else:
    #         rand_count = 5
    #     # print(item_num)
    #     rand_ids = random.sample(range(0, item_num), rand_count)
    #     print('rand_count: %d' % rand_count)
    #     print('item_num: %d' % item_num)
    #     print(rand_ids)
    #     print(models.Item.objects.filter(categories=2))
    #     # context['random_category_item'] = models.Item.objects.filter(categories__in=rand_ids)
    #     return context


