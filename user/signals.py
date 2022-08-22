import email
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

def profileupdate(sender, created, instance, **kwarg):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name)

        print('profile created')
        

post_save.connect(profileupdate, sender=User)