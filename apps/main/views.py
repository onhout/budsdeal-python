import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from apps.products import models

client = settings.ES_CLIENT


# Create your views here.


def main_index(request):
    featured_list = models.Item.objects.all().order_by('-view_count')[:5]
    featured_image = []
    for item in featured_list:
        featured_image.append(item.image_item.filter(primary=True))
    featured_list.item_image = featured_image

    categorized_product = []
    categories = models.Category.objects.filter(parent_category__isnull=True)
    for category in categories:
        child = models.Category.objects.filter(parent_category_id=category.id)
        items = models.Item.objects.filter(categories__id__in=child.values_list('id')).distinct().order_by(
            'view_count')[:5]
        items.parent_category = category
        categorized_product.append(items)

    return render(request, 'index.html', {
        'featured_list': featured_list,
        'categorized_list': categorized_product
    })


def search_product(request):
    from_num = (int(request.GET.get('page', '0')) - 1) * int(request.GET.get('count')) \
        if int(request.GET.get('page')) > 0 else 0
    type_query = ' AND (type:' + request.GET.get('type') + ')' if request.GET.get('type') else ''
    category_query = ' AND(categories.slug:' + request.GET.get('category') + ')' if request.GET.get('category') else ''
    search_query = request.GET.get('search') + "*" if request.GET.get('search') else ''
    _query = search_query + type_query + category_query
    resp = client.msearch(
        index='django',
        body=[
            {"type": "item"},
            {"query": {
                "query_string": {
                    'fields': ['name^3', 'description', 'brand'],
                    'query': _query
                }
            },
                'size': request.GET.get('count'),
                'from': from_num
            }
        ]
    )
    options = json.dumps(
        [{
             'product_id': i['_id'],
             'name': i['_source']['name'],
             'description': i['_source']['description'],
             'brand': i['_source']['brand'],
             'type': i['_source']['type'],
             'category': i['_source']['categories']['name']
         } for i in resp['responses'][0]['hits']['hits']]
    )
    mimetype = 'application/json'
    return HttpResponse(options, mimetype)
