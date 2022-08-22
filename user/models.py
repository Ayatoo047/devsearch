from distutils.command.upload import upload
import email
from email.policy import default
from pyexpat import model
from django.db import models
import uuid
from django.contrib.auth.models import User
from numpy import short


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=2000, blank=True)
    email = models.EmailField(max_length=2000, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to = "profiles/", default = 'profiles/user-default.png')
    location = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(null=True, blank=True, max_length=200)
    short_intro = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    social_link = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

