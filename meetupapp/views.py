from django.shortcuts import render
from django.contrib import auth
from . models import Meetup
from .forms import CreateUserForm, MeetupForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'members/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'members/login.html', context)


def logout(request):
    auth.logout(request)
    return render(request,'base/home.html')


def homePage(request):
    meetups = Meetup.objects.all()
    context = {'meetups': meetups}
    return render(request, 'base/home.html', context)



def meetupPage(request, pk):
    meetup = Meetup.objects.get(id=pk)
    context = {'meetups': meetup}
    return render(request, 'base/meetup.html', context)


def addEvent(request):
    form = MeetupForm()
    if request.method == 'POST':
        form = MeetupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/meetup_form.html', context)