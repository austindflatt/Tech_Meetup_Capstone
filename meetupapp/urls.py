from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),
    path('events/<str:pk>/', views.meetupPage, name="event"),
    path('add-event/', views.addEvent, name="add-event"),
]