from atexit import register
from django.contrib import admin
from .models import Project, Reviews, Tags

# Register your models here.
admin.site.register(Project)
admin.site.register(Reviews)
admin.site.register(Tags)