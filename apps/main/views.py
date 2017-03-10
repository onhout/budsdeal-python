from django.shortcuts import render

from apps.products import models


# Create your views here.


def main_index(request):
    product_list = models.Item.objects.all()
    itemImage = []
    for item in product_list:
        itemImage.append(item.images.all())

    product_list.item_image = itemImage
    return render(request, 'index.html', {
        'product_list': product_list
    })
