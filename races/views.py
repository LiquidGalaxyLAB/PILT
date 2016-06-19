from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, status, serializers
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from races.models import Race,RaceParticipant, Participant
from .forms import RaceForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from .serializers import RaceSerializer,RaceParticipantSerializer, UserSerializer


# Create your views here.

def airview(request):
    race = Race()
    races = Race.objects.all().filter(type=1)
    return render(request,'races/air_race.html', {'races':races})

def groundview(request):
    race=Race()
    races=Race.objects.all().filter(type=0)
    return render(request,'races/ground_race.html',{'races':races})


def detail_race(request,pk):
    race = get_object_or_404(Race, pk=pk)
    return render(request, 'races/detail_race.html', {'race': race})

@csrf_exempt
def new_race(request):
    form = RaceForm()
    if request.method == "POST":
        form = RaceForm(request.POST, request.FILES)
        if form.is_valid():
            race = form.save(commit=False)
            race.save()
            return redirect('races:detail_race', pk=race.pk)
    return render(request, 'races/new_race.html', {'form': form})



def delete_race(request,pk):
    race=Race.objects.get(pk=pk)
    url_destination = race.type
    race.delete()
    if url_destination == 0:
        return HttpResponseRedirect('/ground_race')
    else:
        return HttpResponseRedirect('/air_race')

def edit_race(request,pk):
    race=Race.objects.get(pk=pk)
    form = RaceForm(instance=race)
    if request.method == 'POST':
        form = RaceForm(request.POST, instance=race)
        if form.is_valid():
            drone = form.save(commit=False)
            drone.save()
            if race.type == 0:
                return HttpResponseRedirect('/ground_race')
            else:
                return HttpResponseRedirect('/air_race')
    return render(request, 'races/new_race.html', {'form': form})

@csrf_exempt
def create_participant(request):
    print("---------")
    #name=request.GET.get('name','')

    if request.method == 'POST':
        print("fhgjhk")
        name=request.POST.get('name','')
        image=request.POST.get('image','')
        user = User()
        user.username= name
        user.first_name = name
        user.password = ''
        user.save()
        participant = Participant()
        participant.user = user
        participant.image = image
        participant.save()

    return HttpResponseRedirect('/')


def create_raceparticipant(request,participant,race):
    if request.method == 'POST':
        participant=request.POST.get('')
        participant = Participant()



#Serializers
class RaceViewSet(viewsets.ModelViewSet):
    queryset=Race.objects.all()
    serializer_class = RaceSerializer

class RaceParticipantViewSet(viewsets.ModelViewSet):
    queryset=RaceParticipant.objects.all()
    serializer_class = RaceParticipantSerializer
    print("hola")

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = RaceParticipantSerializer



