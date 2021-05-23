from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about', views.about_page_view, name="about"),
    path('anime', views.anime_page_view, name="anime")
]