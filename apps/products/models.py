from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Item(models.Model):
    TYPE = (
        ('indica', 'Indica'),
        ('sativa', 'Sativa'),
        ('hybrid', 'Hybrid'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=10, choices=TYPE)
    brand = models.CharField(max_length=150, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(blank=True)
    item_pic = models.ImageField(upload_to='./static/media/item_pics', blank=True)
    # TODO change the upload to AMAZON AWS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Item)
def item_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.item_pic:
        instance.item_pic.delete(False)