from django.shortcuts import render

from apps.products import models


# Create your views here.


def main_index(request):
    featured_list = models.Item.objects.all().order_by('-view_count')[:5]
    featured_image = []
    for item in featured_list:
        featured_image.append(item.images.all())

    featured_list.item_image = featured_image

    return render(request, 'index.html', {
        'featured_list': featured_list
    })
