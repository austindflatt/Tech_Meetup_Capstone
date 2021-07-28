from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from . models import Meetup, Job

# Register your models here.

admin.site.register(Meetup)
admin.site.register(Job)


class MeetupAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }