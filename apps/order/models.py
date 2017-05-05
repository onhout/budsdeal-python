from uuid import uuid4

from django.contrib.auth.admin import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from apps.products.models import Item
from apps.user.models import Shipping


# Create your models here.

class Order(models.Model):
    SHIP_METHODS = [
        ('pick', 'pick'),
        ('one', 'one'),
        ('shipping', 'shipping'),
        ('method', 'method'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    total = models.FloatField(null=True, blank=True)
    shipping_address = models.ForeignKey(Shipping, related_name='shipping_address')
    shipping_method = models.CharField(max_length=255, blank=True, null=True, choices=SHIP_METHODS)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    order_status = models.CharField(max_length=10, default='pending')
    editable = models.ForeignKey(User, related_name='editable_user')
    timestamp = models.DateTimeField(auto_now=True)  # LAST UPDATED


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='related_order')
    item = models.ForeignKey(Item, related_name='order_item', blank=True, null=True)
    item_amount = models.IntegerField()
    item_subtotal = models.FloatField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Messages(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='message_regard_order')
    sender = models.ForeignKey(User, related_name='message_sender')
    content = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=Order)
def create_messages_list(sender, instance, created, **kwargs):
    if created:
        Messages.objects.create(order=instance, sender=instance.buyer, content="I'm interested!")


@receiver(pre_save, sender=OrderItems)
def add_subtotal(sender, instance, **kwargs):
    instance.item_subtotal = instance.item_amount * instance.item.price
    order = Order.objects.get(id=instance.order.id)
    if not order.total:
        order.total = instance.item_subtotal
    else:
        order.total += instance.item_subtotal
    order.save()
