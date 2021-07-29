from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Meetup, Job


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MeetupForm(ModelForm):
    class Meta:
        model = Meetup
        fields = ['title', 'thumbnail', 'topic', 'description', 'city', 'address', 'meetup_date', 'creator']

    def __init__(self, *args, **kwargs):
        super(MeetupForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['thumbnail'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['topic'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['city'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['meetup_date'].widget.attrs.update(
            {'class': 'form-control',
             'type': 'datetime-local'}
        )


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location', 'type', 'link']

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['company'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['location'].widget.attrs.update(
            {'class': 'form-control'}
        )