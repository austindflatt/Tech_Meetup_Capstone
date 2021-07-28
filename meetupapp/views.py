from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from . models import Meetup, Job
from .forms import CreateUserForm, MeetupForm, JobForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from . filters import MeetupFilter, eventsFilter
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.


def GoToMeetup(request, pk):
    meetup = get_object_or_404(Meetup, id=request.POST.get('meetup_id'))
    followed = False
    if meetup.followers.filter(id=request.user.id).exists():
        meetup.followers.remove(request.user)
        followed = False
    else:
        meetup.followers.add(request.user)
        followed = True
    return HttpResponseRedirect(reverse('event', args=[str(pk)]))


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

    homeFilter = MeetupFilter(request.GET, queryset=meetups)
    meetups = homeFilter.qs

    context = {'meetups': meetups, 'homeFilter': homeFilter}
    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def allMeetups(request):
    meetups = Meetup.objects.all()

    allEventsFilter = eventsFilter(request.GET, queryset=meetups)
    meetups = allEventsFilter.qs

    context = {'meetups': meetups, 'allEventsFilter': allEventsFilter}
    return render(request, 'base/events.html', context)


@login_required(login_url='login')
def meetupPage(request, pk):
    meetup = Meetup.objects.get(id=pk)
    event_object = Meetup.objects.get(id=pk)
    event_object.blog_views = event_object.event_views+1
    event_object.save()
    stuff = get_object_or_404(Meetup, id=pk)
    total_people = stuff.total_people()
    followed = False
    if stuff.followers.filter(id=request.user.id).exists():
        followed = True
    context = {'meetups': meetup, 'total_people': total_people, 'followed': followed}
    return render(request, 'base/meetup.html', context)


@login_required(login_url='login')
def addEvent(request):
    form = MeetupForm()
    if request.method == 'POST':
        user = request.user
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


@login_required(login_url='login')
def allJobs(request):
    jobs = Job.objects.all()

    context = {'jobs': jobs}
    return render(request, 'base/jobs.html', context)


@login_required(login_url='login')
def jobPage(request, pk):
    job = Job.objects.get(id=pk)
    context = {'job': job}
    return render(request, 'base/job.html', context)


@login_required(login_url='login')
def addJob(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/job_form.html', context)


@login_required(login_url='login')
def editJob(request, pk):
    job = Job.objects.get(id=pk)
    form = MeetupForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/job_form.html', context)


@login_required(login_url='login')
def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    all_jobs = Job.objects.all()
    context = {
        'all_jobs': all_jobs
    }
    return redirect('home')