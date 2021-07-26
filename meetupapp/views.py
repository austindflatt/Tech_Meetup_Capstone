from django.shortcuts import render, redirect
from django.contrib import auth
from . models import Meetup
from .forms import CreateUserForm, MeetupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user + '!')

                return redirect('home')
        context = {'form':form}
        return render(request, 'members/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return redirect('login')
        context = {}
        return render(request, 'members/login.html', context)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')


def homePage(request):
    meetups = Meetup.objects.all()
    context = {'meetups': meetups}
    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def meetupPage(request, pk):
    meetup = Meetup.objects.get(id=pk)
    context = {'meetups': meetup}
    return render(request, 'base/meetup.html', context)


@login_required(login_url='login')
def addEvent(request):
    form = MeetupForm()
    if request.method == 'POST':
        form = MeetupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/meetup_form.html', context)


@login_required(login_url='login')
def editEvent(request, pk):
    event = Meetup.objects.get(id=pk)
    form = MeetupForm(instance=event)
    if request.method == 'POST':
        form = MeetupForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/meetup_form.html', context)


@login_required(login_url='login')
def deleteEvent(request, pk):
    event = Meetup.objects.get(id=pk)
    event.delete()
    all_events = Meetup.objects.all()
    context = {
        'all_events': all_events
    }
    return redirect('home')