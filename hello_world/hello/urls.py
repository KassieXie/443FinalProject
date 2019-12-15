#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.login, name="login"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('student/', views.studentdetails, name="student"),
    path('studentinfo/', views.studentinfo, name="studentinfo"),
]
