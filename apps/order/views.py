import datetime
import json

from channels import Group
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.products.models import Item, ItemImage
from . import forms, models
from .decorators import user_has_order


# Create your views here.


@login_required
def list_orders(request):
    sell_order = models.Order.objects.filter(seller=request.user)
    buy_order = models.Order.objects.filter(buyer=request.user)
    return render(request, 'orders/list_orders.html', {
        'sell_order': sell_order,
        'buy_order': buy_order
    })


@login_required
@user_has_order
def view_order(request, order_id):
    order = models.Order.objects.get(id=order_id)
    order_form = forms.OrderForm(instance=order, user=request.user)
    order_items_forms = forms.OrderItemsFormSet(queryset=models.OrderItems.objects.filter(order=order))
    for item in order_items_forms:
        item.instance.primary_photo = item.instance.item.image_item.filter(primary=True)[0].image
    messages = models.Messages.objects.filter(order=order).order_by('-timestamp')[:25][::-1]
    shipping_addresses = models.Shipping.objects.filter(user=order.buyer)
    if order.order_status == 'confirmed':
        totalobject = {
            "subtotal": "$%.2f" % order.total,
            "tax_rate": "15%",
            "tax": '$%.2f' % (order.total * 0.15),
            "grand_total": '$%.2f' % (order.total * 1.15),
        }
        return render(request, 'orders/confirmed_order.html', {
            'order': order,
            # 'order_items': order_items,
            'order_items_forms': order_items_forms,
            'messages': messages,
            'totals': totalobject,
            'shipping_addresses': shipping_addresses
        })
    else:
        return render(request, 'orders/view_order.html', {
            'order': order,
            # 'order_items': order_items,
            'order_items_forms': order_items_forms,
            'regard_item': order_items_forms[0].instance.item,
            'order_form': order_form,
            'messages': messages,
            'shipping_addresses': shipping_addresses
        })


@login_required
def create_order(request, item_id):
    regard_item = Item.objects.get(id=item_id)
    if regard_item.user == request.user:
        return redirect('/products/list')
    primary_photo = regard_item.image_item.filter(primary=True)
    order_form = forms.OrderForm(user=request.user)
    order_item_form = forms.OrderItemsForm(user=request.user)
    shipping_addresses = models.Shipping.objects.filter(user=request.user)
    return render(request, 'orders/create_order.html', {
        'order_form': order_form,
        'order_item_form': order_item_form,
        'regard_item': regard_item,
        'primary_photo': primary_photo,
        'shipping_addresses': shipping_addresses
    })


@login_required
@user_has_order
def confirm_order(request, order_id):
    order = models.Order.objects.get(id=order_id)
    if request.user.is_authenticated and order.order_status == 'pending':
        order.confirmed_date = datetime.datetime.now()
        order.order_status = 'confirmed'
        order.save()
        Group("order-%s" % order_id).send({
            "text": json.dumps({
                "display_name": request.user.profile.display_name,
                "profile_pic": '/%s' % request.user.profile.profile_photo,
                "full_name": request.user.get_full_name(),
                "msg": "%s has confirmed the order" % request.user.get_full_name()
            })
        })
        models.Messages.objects.create(order=order, sender=request.user,
                                       content="%s has confirmed the order" % request.user.get_full_name())
    return redirect('list_orders')


@login_required
@user_has_order
def cancel_order(request, order_id):
    order = models.Order.objects.get(id=order_id)
    if request.user.is_authenticated and order.order_status == 'pending':
        Group("order-%s" % order_id).send({
            "text": json.dumps({
                "display_name": request.user.profile.display_name,
                "profile_pic": '/%s' % request.user.profile.profile_photo,
                "full_name": request.user.get_full_name(),
                "msg": "%s has canceled the order" % request.user.get_full_name()
            })
        })
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
        'messages': messages
    })


@login_required
@user_has_order
def send_message(request, order_id):
    order = models.Order.objects.get(id=order_id)
    if request.POST and request.user.is_authenticated and order.buyer or order.seller is request.user:
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
    if request.method == "POST" and request.user.is_authenticated:
        try:
            item = Item.objects.get(id=request.GET.get('item'))
            if item.user == request.user:
                return redirect('list_orders')
            else:
                order_form = forms.OrderForm(request.POST, user=request.user, prefix='order_form')
                order_items_form = forms.OrderItemsForm(request.POST, prefix='order_items_form', user=request.user)
            if order_form.is_valid() and order_items_form.is_valid():
                o_form = order_form.save(commit=False)
                i_form = order_items_form.save(commit=False)
                o_form.buyer = request.user
                o_form.seller = item.user
                o_form.editable = item.user
                i_form.item = item
                i_form.order = o_form
                o_form.save()
                i_form.save()
                return redirect('view_order', order_id=o_form.id)
        except:
            order = models.Order.objects.get(id=request.GET.get('order'))
            order_form = forms.OrderForm(request.POST, user=request.user, instance=order, prefix='order_form')
            order_items_forms = forms.OrderItemsFormSet(request.POST,
                                                        queryset=models.OrderItems.objects.filter(order=order))
            if order_form.is_valid() and order_items_forms.is_valid():
                o_form = order_form.save(commit=False)
                Group("order-%s" % order.id).send({
                    "text": json.dumps({
                        "display_name": request.user.profile.display_name,
                        "profile_pic": '/%s' % request.user.profile.profile_photo,
                        "full_name": request.user.get_full_name(),
                        "msg": "%s has made changes to the order" % request.user.get_full_name()
                    })
                })
                models.Messages.objects.create(order=order, sender=request.user,
                                               content="%s has made changes to the order" % request.user.get_full_name())
                if order.buyer == request.user:
                    o_form.editable = order.seller
                elif order.seller == request.user:
                    o_form.editable = order.buyer
                total = 0
                for f in order_items_forms:
                    cd = f.cleaned_data
                    total += cd.get('item_amount') * f.instance.item.price

                o_form.total = total
                o_form.save()
                order_items_forms.save()
                return redirect('view_order', order_id=o_form.id)
        raise PermissionDenied


@login_required
@user_has_order
def list_seller_products(request, order_id):
    order = models.Order.objects.get(id=order_id)
    order_items = models.OrderItems.objects.filter(order=order)
    id_to_exclude = [o.item.id for o in order_items]
    user_product_list = order.seller.product.exclude(id__in=id_to_exclude)
    paginator = Paginator(user_product_list, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    data = []
    for item in products:
        try:
            image = ItemImage.objects.filter(item=item, primary=True)[0].image
        except:
            image = ''

        data.append({
            'id': item.id,
            'name': item.name,
            'type': item.type,
            'min_count': item.min_count,
            'weight_unit': item.weight_unit,
            'price': item.price,
            'primary_photo': str(image)
        })
    return JsonResponse({'data': data})


@login_required
@user_has_order
def add_to_order(request, order_id):
    order = models.Order.objects.get(id=order_id)
    if request.method == "POST" and request.GET.get('item_id'):
        item = Item.objects.get(id=request.GET.get('item_id'))
        order_item_form = forms.OrderItemsForm(request.POST,
                                               prefix='order_items_form',
                                               user=request.user)
        if order_item_form.is_valid():
            form = order_item_form.save(commit=False)
            form.item = item
            form.order = order
            form.save()
            Group("order-%s" % order.id).send({
                "text": json.dumps({
                    "display_name": request.user.profile.display_name,
                    "profile_pic": '/%s' % request.user.profile.profile_photo,
                    "full_name": request.user.get_full_name(),
                    "msg": "%s added %s to the order" % (request.user.get_full_name(), item.name)
                })
            })
            models.Messages.objects.create(order=order, sender=request.user,
                                           content="%s added %s to the order" % (
                                               request.user.get_full_name(), item.name))

            data = {"status": "success"}
            return JsonResponse(data)
        return JsonResponse({"status": "failed"})


@login_required
@user_has_order
def remove_from_order(request, order_id):
    order = models.Order.objects.get(id=order_id)
    if request.GET.get('item_id'):
        item = Item.objects.get(id=request.GET.get('item_id'))
        models.OrderItems.objects.get(order=order, item=item).delete()
        Group("order-%s" % order.id).send({
            "text": json.dumps({
                "display_name": request.user.profile.display_name,
                "profile_pic": '/%s' % request.user.profile.profile_photo,
                "full_name": request.user.get_full_name(),
                "msg": "%s removed %s from the order" % (request.user.get_full_name(), item.name)
            })
        })
        models.Messages.objects.create(order=order, sender=request.user,
                                       content="%s removed %s from the order" % (
                                           request.user.get_full_name(), item.name))

    return redirect('view_order', order_id=order_id)
