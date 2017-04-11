import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.products.models import Item
from . import forms, models


# Create your views here.


@login_required
def list_orders(request):
    own_items = Item.objects.filter(user=request.user)
    sell_order = models.Order.objects.filter(item__in=own_items)
    buy_order = models.Order.objects.filter(buyer=request.user)
    return render(request, 'list_orders.html', {
        'sell_order': sell_order,
        'buy_order': buy_order
    })


@login_required
def view_order(request, order_id):
    order = models.Order.objects.get(id=order_id)
    order_form = forms.OrderForm(instance=order)
    primary_photo = order.item.image_item.filter(primary=True)
    messages = models.Messages.objects.filter(order=order)
    message_form = forms.MessageForm()
    return render(request, 'view_order.html', {
        'order': order,
        'regard_item': order.item,
        'primary_photo': primary_photo,
        'order_form': order_form,
        'messages': messages,
        'message_form': message_form
    })


@login_required
def create_order(request, item_id):
    regard_item = Item.objects.get(id=item_id)
    primary_photo = regard_item.image_item.filter(primary=True)
    order_form = forms.OrderForm()
    return render(request, 'create_quote.html', {
        'order_form': order_form,
        'regard_item': regard_item,
        'primary_photo': primary_photo
    })


@login_required
def send_message(request, order_id):
    order = models.Order.objects.get(id=order_id)
    if request.POST and request.user.is_authenticated and order.buyer or order.item.user is request.user:
        message_form = forms.MessageForm(request.POST)
        if message_form.is_valid():
            form = message_form.save(commit=False)
            form.order = order
            form.sender = request.user
            form.save()
        data = {'status': 'success',
                'content': message_form.content,
                'timestamp': datetime.datetime.now().strftime('%B %d, %Y, %I:%M:%S %p')
                }

    else:
        data = {'status': 'not authorized'}
    return JsonResponse(data)


@login_required
def update_or_create(request):
    if request.POST and request.user.is_authenticated:
        try:
            item = Item.objects.get(id=request.GET.get('item'))
            if item.user == request.user:
                return redirect('list_orders')
            else:
                order_form = forms.OrderForm(request.POST)
            if order_form.is_valid():
                o_form = order_form.save(commit=False)
                o_form.buyer = request.user
                o_form.item = item
                o_form.save()
                return redirect('list_orders')
        except:
            order = models.Order.objects.get(id=request.GET.get('order'))
            order_form = forms.OrderForm(request.POST, instance=order)
            if order_form.is_valid():
                o_form = order_form.save(commit=False)
                o_form.save()
                return redirect('list_orders')
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
