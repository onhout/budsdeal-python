from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


#
#
# # Create your models here.
#
#
class UserProfile(models.Model):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, null=True, blank=True,
                              choices=GENDERS)
    locale = models.CharField(max_length=10, blank=True, null=True)

    facebook_id = models.CharField(max_length=255, blank=True)

    profile_photo = models.ImageField(upload_to='./user_profiles_pics')
    # TODO change the upload to AMAZON AWS

    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
