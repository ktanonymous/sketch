from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
]