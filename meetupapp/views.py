from django.shortcuts import render
from . models import Meetup
from .forms import MeetupForm

# Create your views here.


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