from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.products.models import Item
from . import forms


# Create your views here.


@login_required
def list_orders(request):
    return render(request, 'list_orders.html', {

    })


@login_required
def create_order(request, item_id):
    regard_item = Item.objects.get(id=item_id)
    primary_photo = regard_item.image_item.filter(primary=True)
    if request.POST and request.user.is_authenticated:
        order_form = forms.OrderForm(request.POST)
        if order_form.is_valid():
            o_form = order_form.save(commit=False)
            o_form.buyer = request.user
            o_form.item = regard_item
            o_form.save()
            return redirect('create_order')
    else:
        order_form = forms.OrderForm()
    return render(request, 'create_quote.html', {
        'order_form': order_form,
        'regard_item': regard_item,
        'primary_photo': primary_photo
    })

    #
    # @login_required
    # def send_message(request, social_id, item_id):
    #     user_profile = Profile.objects.get(social_id=social_id)
    #     this_user = User.objects.get(id=user_profile.user_id)
    #     regard_item = Item.objects.get(id=item_id)
    #     if request.POST and request.user.is_authenticated:
    #         message_form = forms.MessageForm(request.POST)
    #         if message_form.is_valid():
    #             form = message_form.save(commit=False)
    #             form.from_user = request.user
    #             form.to_user = this_user
    #             form.regard_item = regard_item
    #             form.save()
    #             return redirect('view_sent_messages')
    #     else:
    #         message_form = forms.MessageForm(initial={'subject': 'Quote regarding: ' + regard_item.name})
    #
    #     return render(request, 'user/send_message.html', {
    #         'this_product': regard_item,
    #         'this_user': this_user,
    #         'message_form': message_form
    #     })
