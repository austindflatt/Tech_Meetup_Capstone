import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    topic = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    meetup_date = models.DateTimeField()
    followers = models.ManyToManyField(User, related_name="meetuppost")
    created = models.DateTimeField(auto_now_add=True)
    event_views = models.IntegerField(default=0)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def total_people(self):
        return self.followers.count()

    def __str__(self):
        return self.title + ' | ' + str(self.creator)


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Member(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    def __str__(self):
        return self.name