from django.db import models
from django.contrib.auth.admin import User

# Create your models here.


class Conversations(models.Model):
    from_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user_id')
    to_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_id')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
