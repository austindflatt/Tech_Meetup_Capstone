from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),
    path('events/', views.allMeetups, name="events"),
    path('jobs/', views.allJobs, name="jobs"),
    path('going/<str:pk>', views.GoToMeetup, name="going"),
    path('users/', views.showUsers, name="users"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logout, name='logout'),

    path('events/<str:pk>/', views.meetupPage, name="event"),
    path('add-event/', views.addEvent, name="add-event"),
    path('edit-event/<str:pk>/', views.editEvent, name="edit-event"),
    path('delete-event/<str:pk>/', views.deleteEvent, name="delete-event"),

    path('jobs/<str:pk>/', views.jobPage, name="job"),
    path('add-job/', views.addJob, name="add-job"),
    path('edit-job/<str:pk>/', views.editJob, name="edit-job"),
    path('delete-job/<str:pk>/', views.deleteJob, name="delete-job"),
]