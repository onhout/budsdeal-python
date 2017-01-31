from django.db import models
from datetime import datetime
from rest_framework import serializers

# Create your models here.


class User(object):
    def __init__(self, email, password, created=None):
        self.email = email
        self.password = password,
        self.created = created or datetime.now()


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
