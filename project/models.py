from contextlib import nullcontext
from email.policy import default
from enum import unique
from unicodedata import name
from venv import create
from django.db import models
from user.models import Profile
import uuid

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    tags = models.ManyToManyField('Tags', blank=True)
    vote_total = models.IntegerField(null=True, blank=True)
    vote_ratio = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    source_link = models.TextField(max_length=2000, null=True, blank=True)
    demo_link = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['created']

    @property
    def getVoteCount(self):
        reviews = self.review_set.all() 
        upVotes = reviews.filter(value="up").count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=2000, blank=True, null=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['project', 'owner']]

    def __str__(self):
        return str(self.value)

    


class Tags(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name




    
