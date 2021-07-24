import uuid

from django.db import models

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    topic = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    meetup_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title

