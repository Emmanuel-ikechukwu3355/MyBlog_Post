from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# def create_or_update_user_profile(sender, instance, created, **Kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()

# Create your models here.
