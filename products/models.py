from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


class Item(models.Model):
    TYPE = (
        ('indica', 'Indica'),
        ('sativa', 'Sativa'),
        ('hybrid', 'Hybrid'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, null=True)
    type = models.CharField(max_length=10, null=True, blank=True, choices=TYPE)
    brand = models.CharField(max_length=150, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(blank=True)
    item_pic = models.ImageField(upload_to='./static/media/item_pics', blank=True, null=True)
    # TODO change the upload to AMAZON AWS

    def __str__(self):
        return self.name