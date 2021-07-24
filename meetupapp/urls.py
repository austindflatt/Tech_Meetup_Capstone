from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logout, name='logout'),

    path('events/<str:pk>/', views.meetupPage, name="event"),
    path('add-event/', views.addEvent, name="add-event"),
]