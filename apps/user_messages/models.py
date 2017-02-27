from django.db import models
from django.contrib.auth.admin import User
from apps.products.models import Item
from uuid import uuid4


# Create your models here.


class Conversations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    from_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user_id')
    to_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_id')
    regard_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='regard_item')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
