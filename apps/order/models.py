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
    item = models.ForeignKey(Item, related_name='order_item')
    total = models.FloatField(null=True, blank=True)
    item_amount = models.IntegerField()
    shipping_address = models.ForeignKey(Shipping, blank=True, null=True, related_name='shipping_address')
    shipping_method = models.CharField(max_length=255, blank=True, null=True, choices=SHIP_METHODS)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    order_status = models.CharField(max_length=10, default='pending')
    timestamp = models.DateTimeField(auto_now=True)


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


@receiver(pre_save, sender=Order)
def add_total(sender, instance, **kwargs):
    instance.total = instance.item_amount * instance.item.price