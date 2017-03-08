import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    parent_category = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    TYPE = [
        ('indica', 'Indica'),
        ('sativa', 'Sativa'),
        ('hybrid', 'Hybrid'),
    ]
    WEIGHT_UNIT = [
        ('gram', 'g'),
        ('kilogram', 'kg'),
        ('ounce', 'oz'),
        ('pounds', 'lb'),
        ('unit', 'unit'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=10, choices=TYPE)
    brand = models.CharField(max_length=150, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    count = models.DecimalField(max_digits=9, decimal_places=2)
    weight_unit = models.CharField(max_length=10, choices=WEIGHT_UNIT)
    categories = models.ForeignKey(Category, related_name='categories')
    description = models.TextField(blank=True)
    # TODO change the upload to AMAZON AWS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def get_file_path(instance, filename):
    filename = '%s.%s' % (uuid4(), 'jpg')
    return os.path.join(instance.directory_string, filename)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to=get_file_path,
                                processors=[ResizeToFill(640, 480)],
                                format='JPEG')
    directory_string = './static/media/item_pics'


@receiver(post_delete, sender=ItemImage)
def image_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)


@receiver(pre_save, sender=ItemImage)
def image_update(sender, instance, **kwargs):
    try:
        old_item = ItemImage.objects.get(pk=instance.id)
        if old_item.image:
            old_item.image.delete(False)
    except ItemImage.DoesNotExist:
        pass
