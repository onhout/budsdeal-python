from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


@login_required
def add_product(request):
    if request.method == 'POST':
        product_form = forms.AddProductForm(request.POST, instance=request.user)
        if product_form.is_valid():
            product_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('user_settings')
            # else:
            # messages.error(request, _('Please correct the error below.'))
    else:
        product_form = forms.AddProductForm(instance=request.user)

    return render(request, 'add_products.html', {
        'add_product_form': product_form
    })
