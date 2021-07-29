import django_filters
from . models import *


class MeetupFilter(django_filters.FilterSet):
    class Meta:
        model = Meetup
        fields = '__all__'
        exclude = ['title', 'thumbnail', 'description', 'slug', 'id', 'created', 'followers', 'event_views', 'creator', 'lat', 'long']


class eventsFilter(django_filters.FilterSet):
    class Meta:
        model = Meetup
        fields = '__all__'
        exclude = ['title', 'thumbnail', 'description', 'slug', 'id', 'created']
