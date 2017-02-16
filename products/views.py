from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from uuid import uuid4

from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify

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
            # messages.success(request, _('Your profile was successfully updated!'))
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
    return render(request, 'list_products.html', {
        'product_list': product_list
    })
