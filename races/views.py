from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def airview(request):
    return render(request,'races/air_race.html', {})

def groundview(request):
    return render(request,'races/ground_race.html', {})
