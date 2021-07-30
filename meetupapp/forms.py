from django.forms import ModelForm, DateTimeInput
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
        fields = ['title', 'thumbnail', 'topic', 'description', 'city', 'address', 'meetup_date', 'end_date', 'creator']

        widgets = {
            'meetup_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(MeetupForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'placeholder': 'Choose a title for your event'}
        )
        self.fields['topic'].widget.attrs.update(
            {'placeholder': 'What topic will be discussed?'}
        )
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Please give a detailed description of what this event is about'}
        )
        self.fields['city'].widget.attrs.update(
            {'placeholder': 'What city will this be in?'}
        )
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'What is the address?'}
        )
        self.fields['meetup_date'].widget.attrs.update(
            {'placeholder': 'datetime-local'}
        )
        self.fields['end_date'].widget.attrs.update(
            {'placeholder': 'datetime-local'}
        )
        self.fields['meetup_date'].widget.attrs.update(
            {'class': '',
             'type': 'datetime-local'}
        )


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location', 'type', 'link']

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'placeholder': 'What is the name of the role you are hiring for?'}
        )
        self.fields['company'].widget.attrs.update(
            {'placeholder': 'Company name'}
        )
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Please give a detailed description about this job'}
        )
        self.fields['location'].widget.attrs.update(
            {'placeholder': 'Type an address'}
        )
        self.fields['type'].widget.attrs.update(
            {'placeholder': 'Full time or Part time?'}
        )
        self.fields['link'].widget.attrs.update(
            {'placeholder': 'Company website'}
        )