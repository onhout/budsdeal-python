from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from . import forms, models


# Create your views here.


@login_required
def add_product(request):
    if request.POST and request.user.is_authenticated:
        product_form = forms.AddProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            form = product_form.save(commit=False)
            # NOTE: VARIABLES FROM FORM, SHOULD MAKE ANOTHER VARIABLES JUST FOR THE SAVE
            # THIS IS VERY IMPORTANT!!
            form.user = request.user
            form.item_pic.save(slugify(uuid4().hex + '_i') + '.jpg', request.FILES['item_pic'])
            form.save()
            # product_form.save_m2m()
            return redirect('list_product')
            # else:
            # messages.error(request, _('Please correct the error below.'))
    else:
        product_form = forms.AddProductForm(instance=request.user)

    return render(request, 'add_products.html', {
        'add_product_form': product_form
    })


@login_required
def list_product(request):
    product_list = models.Item.objects.all().filter(user=request.user)
    # if not request.user.company.name: #DISABLED FOR DEVELOPMENT
    #     return redirect('user_settings') #TODO REENABLE IT WHEN EVERYTHING IS DONE
    # else:
    return render(request, 'list_products.html', {
            'product_list': product_list
        })


@login_required
def update_product(request, product_id):
    product = models.Item.objects.get(pk=product_id)
    if request.POST and request.user.is_authenticated:
        product_form = forms.EditProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            form = product_form.save(commit=False)
            # NOTE: VARIABLES FROM FORM, SHOULD MAKE ANOTHER VARIABLES JUST FOR THE SAVE
            # THIS IS VERY IMPORTANT!!
            form.user = request.user
            if request.FILES:
                form.item_pic.save(slugify(uuid4().hex + '_i') + '.jpg', request.FILES['item_pic'])
            form.save()
            # product_form.save_m2m()
            return redirect('list_product')
            # else:
            # messages.error(request, _('Please correct the error below.'))
    else:
        product_form = forms.EditProductForm(instance=product)

    return render(request, 'update_product.html', {
        'product_id': product_id,
        'edit_product_form': product_form
    })


@login_required
def delete_product(request, product_id):
    product = models.Item.objects.get(pk=product_id).delete()
    if request.POST and request.user.is_authenticated:
        product.save()

    return redirect('list_product')


def view_product(request, product_id):
    item = models.Item.objects.get(pk=product_id)
    return render(request, 'view_product.html', {
        'item': item
    })


def parent_categories(request, category_slug):
    parent_category = models.Category.objects.get(slug=category_slug, parent_category__isnull=True)
    child = models.Category.objects.filter(parent_category_id=parent_category.id)
    items = models.Item.objects.filter(categories__id__in=child.values_list('id')).distinct()
    return render(request, 'category_list.html', {
        'items': items
    })


def child_categories(request, category_slug, subcategory_slug):
    child_category = models.Category.objects.filter(slug=subcategory_slug, parent_category__isnull=False)
    items = models.Item.objects.filter(categories=child_category)
    return render(request, 'category_list.html', {
        'items': items
    })
