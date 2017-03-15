from django.shortcuts import render

from apps.products import models


# Create your views here.


def main_index(request):
    featured_list = models.Item.objects.all().order_by('-view_count')[:5]
    featured_image = []
    for item in featured_list:
        featured_image.append(item.images.all())

    featured_list.item_image = featured_image

    product_list = models.Item.objects.all()
    itemImage = []
    for item in product_list:
        itemImage.append(item.images.all())

    product_list.item_image = itemImage
    return render(request, 'index.html', {
        'product_list': product_list,
        'featured_list': featured_list
    })
