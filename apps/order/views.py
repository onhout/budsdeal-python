import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.products.models import Item
from . import forms, models
from .decorators import user_has_order


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
@user_has_order
def view_order(request, order_id):
    order = models.Order.objects.get(id=order_id)
    order_form = forms.OrderForm(instance=order, user=request.user)
    primary_photo = order.item.image_item.filter(primary=True)
    messages = models.Messages.objects.filter(order=order).order_by('-timestamp')[:25][::-1]
    if order.order_status == 'confirmed':
        return render(request, 'confirmed_order.html', {
            'order': order,
            'regard_item': order.item,
            'primary_photo': primary_photo,
            'messages': messages
        })
    else:
        return render(request, 'view_order.html', {
            'order': order,
            'regard_item': order.item,
            'primary_photo': primary_photo,
            'order_form': order_form,
            'messages': messages
        })


@login_required
def create_order(request, item_id):
    regard_item = Item.objects.get(id=item_id)
    primary_photo = regard_item.image_item.filter(primary=True)
    order_form = forms.OrderForm(user=request.user)
    return render(request, 'create_order.html', {
        'order_form': order_form,
        'regard_item': regard_item,
        'primary_photo': primary_photo
    })


@login_required
@user_has_order
def confirm_order(request, order_id):
    order = models.Order.objects.get(id=order_id)
    if request.user.is_authenticated:
        models.Messages.objects.create(order=order, sender=request.user,
                                       content="%s has confirmed the order" % request.user.get_full_name())
        order.order_status = 'confirmed'
        order.save()
    return redirect('list_orders')


@login_required
@user_has_order
def cancel_order(request, order_id):
    order = models.Order.objects.get(id=order_id)
    if request.user.is_authenticated:
        models.Messages.objects.create(order=order, sender=request.user,
                                       content="%s has canceled the order" % request.user.get_full_name())
        order.order_status = 'canceled'
        order.save()
    return redirect('view_order', order_id=order.id)


@login_required
@user_has_order
def view_all_message(request, order_id):
    order = models.Order.objects.get(id=order_id)
    messages = models.Messages.objects.filter(order=order).order_by('timestamp')
    return render(request, 'view_all_message.html', {
        'order': order,
        'regard_item': order.item,
        'messages': messages
    })


@login_required
@user_has_order
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
                o_form.editable = item.user
                o_form.item = item
                o_form.save()
                return redirect('view_order', order_id=o_form.id)
        except:
            order = models.Order.objects.get(id=request.GET.get('order'))
            order_form = forms.OrderForm(request.POST, instance=order)
            if order_form.is_valid():
                o_form = order_form.save(commit=False)
                models.Messages.objects.create(order=order, sender=request.user,
                                               content="%s has made changes to the order" % request.user.get_full_name())
                if order.buyer == request.user:
                    o_form.editable = order.item.user
                elif order.item.user == request.user:
                    o_form.editable = order.buyer
                o_form.save()
                return redirect('view_order', order_id=o_form.id)
        raise PermissionDenied
