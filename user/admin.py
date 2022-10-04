from django.contrib import admin
from .models import Skill, Profile, Message

# Register your models here.
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Message)