from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Meetup


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MeetupForm(ModelForm):
    class Meta:
        model = Meetup
        fields = ['title', 'thumbnail', 'topic', 'description', 'location']

    def __init__(self, *args, **kwargs):
        super(MeetupForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'}
        )