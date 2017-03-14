from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random

#
#
# # Create your models here.
#
#
class Profile(models.Model):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, null=True, blank=True,
                              choices=GENDERS)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    locale = models.CharField(max_length=10, blank=True, null=True)
    social_id = models.CharField(max_length=255, blank=True)
    login_type = models.CharField(max_length=10, null=True, blank=True)
    account_type = models.CharField(max_length=10, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='./static/media/profile_pics')
    id_photo = models.ImageField(upload_to='./static/media/ID_PHOTOS', blank=True)
    approved_as_seller = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO change the upload to AMAZON AWS

    def __str__(self):
        return self.user.username


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    TIN = models.CharField(max_length=255)  # -> Taxpayer Identification Number
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        display_name = instance.first_name.lower() + str(random.randint(1, 10000))
        Profile.objects.create(user=instance, display_name=display_name)
        Company.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.company.save()
