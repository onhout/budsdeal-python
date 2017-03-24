from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, redirect

from . import forms as product_forms, models as product_models


# Create your views here.


def view_product(request, product_id):
    item = product_models.Item.objects.get(pk=product_id)
    if item.user != request.user:
        item.view_count += 1
        item.save()
    return render(request, 'view_product.html', {
        'item': item,
        'item_images': item.images.all()
    })


def parent_categories(request, category_slug):
    parent_category = product_models.Category.objects.get(slug=category_slug, parent_category__isnull=True)
    child = product_models.Category.objects.filter(parent_category_id=parent_category.id)
    items = product_models.Item.objects.filter(categories__id__in=child.values_list('id')).distinct()
    return render(request, 'category_list.html', {
        'items': items
    })


def child_categories(request, category_slug, subcategory_slug):
    child_category = product_models.Category.objects.filter(slug=subcategory_slug, parent_category__isnull=False)
    items = product_models.Item.objects.filter(categories=child_category)
    return render(request, 'category_list.html', {
        'items': items
    })


# USER PRODUCTS
@login_required
def add_product(request):
    if request.POST and request.user.is_authenticated:
        product_form = product_forms.AddProductForm(request.POST)
        # formset = product_forms.AddImageFormSet(request.POST, request.FILES,
        #                                         queryset=product_models.ItemImage.objects.none())
        if product_form.is_valid():  # and formset.is_valid()
            form = product_form.save(commit=False)
            # NOTE: VARIABLES FROM FORM, SHOULD MAKE ANOTHER VARIABLES JUST FOR THE SAVE
            # THIS IS VERY IMPORTANT!!
            form.user = request.user
            form.save()
            # for formset in formset.cleaned_data:
            #     try:
            #         image = formset['image']
            #         photo = product_models.ItemImage(item=form, image=image)
            #         photo.save()
            #     except:
            #         pass
            return redirect('image_upload', product_id=form.id)
    elif request.user.profile.approved_as_seller:
        product_form = product_forms.AddProductForm(instance=request.user)
        # formset = product_forms.AddImageFormSet(queryset=product_models.ItemImage.objects.none())
    else:
        return redirect('register_as_seller')
    return render(request, 'user/add_products.html', {
        'add_product_form': product_form,
        # 'formset': formset
    })


@login_required
def image_upload(request, product_id):
    item = product_models.Item.objects.get(id=product_id)
    if request.POST and request.user.is_authenticated and request.user.profile.approved_as_seller:
        image_form = product_forms.ImageForm(request.POST, request.FILES)
        if image_form.is_valid() and request.user == item.user:
            form = image_form.save(commit=False)
            form.item = item
            form.save()
            data = {'is_valid': True, 'name': form.item.name, 'url': '/' + form.image.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
    return render(request, 'user/image_upload.html', {
        'item': item
    })


@login_required
def list_product(request):
    product_list = product_models.Item.objects.all().filter(user=request.user)
    paginator = Paginator(product_list, 5)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    itemImage = []
    for item in products:
        itemImage.append(item.images.all())

    products.item_image = itemImage
    if not request.user.company.name and request.user.profile.approved_as_seller:  # DISABLED FOR DEVELOPMENT
        return redirect('user_company')  # TODO REENABLE IT WHEN EVERYTHING IS DONE
    elif not request.user.profile.approved_as_seller:
        return redirect('register_as_seller')
    else:
        return render(request, 'user/list_products.html', {
            'product_list': products
        })


@login_required
def update_product(request, product_id):
    product = product_models.Item.objects.get(pk=product_id)
    if request.POST and request.user.is_authenticated:
        product_form = product_forms.EditProductForm(request.POST, request.FILES, instance=product)
        formset = product_forms.UpdateImageFormSet(request.POST, request.FILES, instance=product)
        if product_form.is_valid() and formset.is_valid():
            form = product_form.save(commit=False)
            # NOTE: VARIABLES FROM FORM, SHOULD MAKE ANOTHER VARIABLES JUST FOR THE SAVE
            # THIS IS VERY IMPORTANT!!
            form.user = request.user
            form.save()
            formset.save()
            return redirect('list_product')
    elif request.user.profile.approved_as_seller:
        product_form = product_forms.EditProductForm(instance=product)
        formset = product_forms.UpdateImageFormSet(instance=product)
    else:
        return redirect('register_as_seller')

    return render(request, 'user/update_product.html', {
        'product_id': product_id,
        'edit_product_form': product_form,
        'formset': formset
    })


@login_required
def delete_product(request, product_id):
    product = product_models.Item.objects.get(pk=product_id).delete()
    if request.POST and request.user.is_authenticated and request.user.profile.approved_as_seller:
        product.save()

    return redirect('list_product')
