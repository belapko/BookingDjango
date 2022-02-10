from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.timezone import now
from datetime import timedelta
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)

    activation_key = models.CharField(max_length=128, blank=True)

    def is_activation_key_expired(self):
        return now() - self.date_joined > timedelta(hours=48)

#
# class UserProfile(models.Model):
#     MALE = 'M'
#     FEMALE = 'W'
#     GENDER_CHOICES = (
#         (MALE, 'М'),
#         (FEMALE, 'Ж')
#     )
#     user = models.OneToOneField(User, null=False, db_index=True, on_delete=models.CASCADE)
#     tagline = models.CharField(verbose_name='Тэги', max_length=128, blank=True)
#     gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDER_CHOICES, blank=True)
#
#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.userprofile.save()
#
#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             UserProfile.objects.create(user=instance)