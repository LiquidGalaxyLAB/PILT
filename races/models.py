from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
# Create your models here.
from django.http import HttpResponseRedirect


class Competition(models.Model):
    name=models.CharField(max_length=100)
    imageURL=models.CharField(max_length=100)

class Task(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=100)
    file = models.FileField(upload_to='static/competitions')
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)


class CompetitionTaskParticipant(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE )
    kmlpath = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class CompetitionTaskParticipantPosition(models.Model):
    instant = models.IntegerField(default=0)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    taskparticipant = models.ForeignKey(CompetitionTaskParticipant)


class AirRace(models.Model):
    name=models.CharField(max_length=100)
    folderPath=models.CharField(max_length=100)
    imageURL = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.pk)

class AirRaceParticipant(models.Model):
    airrace = models.ForeignKey(AirRace, on_delete=models.CASCADE,)
    kmlpath = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

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
    image = models.CharField(max_length=200,null=True, blank=True)

class RaceParticipant(models.Model):
    race = models.ForeignKey(Race)
    participant = models.ForeignKey(Participant)
    def __unicode__(self):
        return str(self.pk)

class Position(models.Model):
    instant = models.IntegerField(default=0)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    raceparticipant = models.ForeignKey(RaceParticipant)


