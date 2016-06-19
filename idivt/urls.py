from django.conf.urls import include,url
from django.contrib import admin
from rest_framework import routers
from . import views
from .resources import api



urlpatterns = [
    url(r'^air_race/$', views.airview, name='airrace'),
]