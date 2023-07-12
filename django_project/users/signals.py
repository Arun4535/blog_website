from django.contrib.auth.models import User
from django.db.models.signals import post_save # post_save => it is fired when object is saved
from django.dispatch import receiver
from .models import Profile

@receiver(post_save , sender = User) #when sender is saved it send this signal, is received by this receiver
def create_profile(sender, instance , created , **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save , sender = User)
def save_profile(sender, instance , **kwargs):
    instance.profile.save()