from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Photos(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    twitch_url = models.CharField(max_length=500, null=True, blank=True,)
    youtube_url = models.CharField(max_length=500, null=True, blank=True,)
    discord = models.CharField(max_length=500, null=True, blank=True,)


    def __str__(self):
        return str(self.user)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.CharField(max_length=200)
#     birth_date = models.DateField(null=True, default='1990-01-01', blank=True)
#     gamer_tag = models.CharField(max_length=50)
#     system = models.
#     discord = models.CharField(max_length=50)
#     twitch = models.CharField(max_length=200)
#     bio = models.TextField(max_length=500, default='', blank=False)
#     SYSTEM = (
#         ('PC', 'PC'),
#         ('XBOX', 'Xbox'),
#         ('PLAYSTATION', 'Playstation'),
#         ('SWITCH', 'Switch'),
#         ('OTHER', 'Other'),
#     )
#     LOOKING_FOR = (
#         ('MALE', 'Men'),
#         ('FEMALE', 'Women'),
#         ('BOTH', 'Both'),
#     )
#     APPROVAL = (
#         ('TO BE APPROVED', 'To be approved'),
#         ('APPROVED', 'Approved'),
#         ('NOT APPROVED', 'Not approved')
#     )
#     GENDER = (
#         ("MALE", "Male"),
#         ("FEMALE", "Female")
#         ("OTHER", "Other")
#     )
#     TIMEZONE = (
#         ("EST", "Eastern Time"),
#         ("CT", "Central Time")
#         ("MT", "Mountain Time")
#         ("PT", "Pacific Time")
#     )    
#     gender = models.CharField(choices=GENDER, default="OTHER", max_length=6)
#     looking_for = models.CharField(choices=LOOKING_FOR, default='BOTH', blank=False, max_length=6)
#     is_verified = models.CharField(choices=APPROVAL, default="TO BE APPROVED", blank=False, max_length=14)
#     location = models.CharField(choices=TIMEZONE, default="PT", blank=False, max_length=5)
#     system = models.CharField(choices=SYSTEM, default="OTHER", blank=False, max_length=20)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
