import uuid
import geocoder
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

mapbox_access_token = 'pk.eyJ1IjoiYXVzdGluZmxhdHQiLCJhIjoiY2tyb2Y3YXpjMnBlNTJ1cDZlN2V2bGc4biJ9.3g_h6Pit7Y2VWalrOPxMow'


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    topic = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=200)
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    meetup_date = models.DateTimeField()
    followers = models.ManyToManyField(User, related_name="meetuppost")
    created = models.DateTimeField(auto_now_add=True)
    event_views = models.IntegerField(default=0)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=User)
    slug = models.SlugField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def total_people(self):
        return self.followers.count()

    def __str__(self):
        return self.title + ' | ' + str(self.creator)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Meetup, self).save(*args, **kwargs)


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