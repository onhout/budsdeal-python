from uuid import uuid4

from django.contrib.auth.admin import User
from django.db import models

from apps.products.models import Item


# Create your models here.


class Conversations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    regard_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='regard_item')
    regard_item_amount = models.IntegerField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
