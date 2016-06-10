from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Race(models.Model):
    name = models.CharField(max_length=100)
    Race_Type = [
        (1, 'Air'),
        (0, 'Ground')
    ]

    type=models.IntegerField(choices=Race_Type,default=0)
    image= models.FileField(upload_to='documents/%Y/%m/%d')

    localization_name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    initial_date = models.DateField(verbose_name="Initial date")
    initial_time = models.TimeField(verbose_name="Initial time")


class Participant(models.Model):
    user = models.OneToOneField(User,related_name="profile")
    races = models.ManyToManyField(Race, through='RaceParticipant')


class RaceParticipant(models.Model):
    race = models.ForeignKey(Race)
    participant = models.ForeignKey(Participant)



class Position(models.Model):
    instant = models.DateTimeField(auto_now=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    raceposition = models.ForeignKey(RaceParticipant)





