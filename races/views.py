import os
from os.path import isfile,join

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

from rest_framework import viewsets, status, serializers
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from liquidgalaxy.kml_generator import create_participant_kml, create_routeparticipant_kml, find_between,create_competitiontaskparticipant_kml
from liquidgalaxy.lgCommunication import send_galaxy,write_kml_race, write_kml_participant, write_kml_airrace,send_single_kml,create_kmlstxt
from pilt.settings import BASE_DIR
from races.models import Race,RaceParticipant, Participant, Position, AirRace, AirRaceParticipant, Task,Competition,CompetitionTaskParticipant,CompetitionTaskParticipantPosition
from .forms import RaceForm, AirRaceForm, CompetitionForm, TaskForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from .serializers import RaceSerializer,RaceParticipantSerializer, UserSerializer


# Create your views here.


def competitionview(request):
    competitions = Competition.objects.all()
    return render(request,'races/competition.html', {'competitions':competitions})
def airview(request):
    race = AirRace()
    races = AirRace.objects.all()
    return render(request,'races/air_race.html', {'races':races})
def groundview(request):
    race=Race()
    races=Race.objects.all().filter(type=0)
    return render(request,'races/ground_race.html',{'races':races})
def taskview(request,pk):
    competition = Competition.objects.get(pk=pk)
    tasks = Task.objects.filter(competition=competition)
    return render(request,'races/task.html',{'tasks':tasks})

def detail_airrace(request,pk):
    airrace = AirRace.objects.get(pk=pk)
    airparticipants = AirRaceParticipant.objects.filter(airrace=airrace)
    return render(request, 'races/detail_airrace.html', {'airrace': airrace, 'participants':airparticipants})
def detail_race(request,pk):
    race = get_object_or_404(Race, pk=pk)
    participants = get_all_raceparticipants(race)
    return render(request, 'races/detail_race.html', {'race': race, 'participants':participants})
def detail_competition(request,pk):
    competition = get_object_or_404(Competition, pk=pk)
    tasks = Task.objects.filter(competition=competition)
    return render(request, 'races/detail_competition.html', {'tasks': tasks})
def detail_task(request,competition,task):
    competitiontaskparticipants = CompetitionTaskParticipant.objects.filter(task=task)

    return render(request, 'races/detail_task.html', {'competitiontaskparticipants':competitiontaskparticipants})

def create_tasks_participants(task):
    print(BASE_DIR)
    print(task.file)
    print("---")
    path=BASE_DIR+"/"+task.file.name
    print(path)
    print("---")
    print(task.file.path)

    name=task.file.name.split('/')
    print name
    dirName= name[2].split('.')
    print dirName
    folderPath = dirName[0]
    print folderPath
    print ">------"


    folderPath=BASE_DIR+"/"+folderPath
    os.mkdir(folderPath)

    os.system("unzip %s -d %s" % (task.file, folderPath))

    print folderPath
    #space=" "
    #underbar="_"
    #folderPath= folderPath.replace(underbar,space)
    print folderPath
    print"-----"

    onlyfiles = [f for f in os.listdir(folderPath) if isfile(join(folderPath, f))]
    for file in onlyfiles:
        igcPath = folderPath+"/"+file
        create_competitiontaskparticipant(igcPath, task)

    print folderPath
    os.system("rm -R %s" % (folderPath))
    os.system("rm -R %s" % (path))

    print("hola")
def create_competitiontaskparticipant(file, task):
    lines = [line.rstrip('\n') for line in open(file)]
    substring= "HFPLTPILOT"

    valor = substring in lines[2]
    if valor:
        pilotName = lines[2].strip('HFPLTPILOT: ')
    else:
        pilotName = lines[3].strip('HFPLTPILOTINCHARGE: ')

    print pilotName
    arrayCoordinates = lines[9:len(lines)-3]

    index = 0
    for i,line in enumerate(lines):
        if line[0][0] == 'B':
            arrayCoordinates=lines[i:len(lines)-4]
            break


    competitiontaskparticipant = CompetitionTaskParticipant()
    competitiontaskparticipant.name=pilotName
    competitiontaskparticipant.task = task
    competitiontaskparticipant.save()

    for i in range(1,len(arrayCoordinates),100):
        line=arrayCoordinates[i]
        timeStamp = line[1:7]
        latDMS = line[7:15]
        longDMS = line[15:24]
        altitude = line[25:30]
        latDEC = convert(latDMS)
        longDEC = convert(longDMS)
        position = CompetitionTaskParticipantPosition()
        position.instant = timeStamp
        position.latitude = latDEC
        position.longitude = longDEC
        position.height = altitude
        position.taskparticipant = competitiontaskparticipant
        position.save()
    print competitiontaskparticipant.name
    create_competitiontaskparticipant_kml(competitiontaskparticipant)
def convert(degreeCoordinate):
    cardinalPoint = degreeCoordinate[-1:]


    if str(cardinalPoint) == "N" or str(cardinalPoint) =="S":
        integerPart = degreeCoordinate[2:4]
        decimalPart = degreeCoordinate[4:7]
        minutes=integerPart+"."+decimalPart
        decimalCoordinate = float(degreeCoordinate[0:2]) + float(minutes)/60
        if str(cardinalPoint) == "S":
            decimalCoordinate = float(decimalCoordinate) * -1
    else:

        integerPart = degreeCoordinate[3:5]
        decimalPart = degreeCoordinate[5:8]
        minutes = integerPart + "." + decimalPart

        decimalCoordinate = float(degreeCoordinate[0:3]) + float(minutes)/60
        if str(cardinalPoint) == "W":
            decimalCoordinate = float(decimalCoordinate) * -1
    return decimalCoordinate
def new_task(request,pk):
    form = TaskForm()
    competition = get_object_or_404(Competition, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.competition = competition
            task.save()

            if not os.path.exists("static/kml/" + str(task.competition.pk)):
                os.makedirs("static/kml/" + str(task.competition.pk))

            create_tasks_participants(task)
            return redirect('races:detail_task', task=task.pk,competition=competition.pk)
    return render(request, 'races/new_task.html', {'form': form})
def new_competition(request):
    form = CompetitionForm()
    if request.method == "POST":
        form = CompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            competition = form.save(commit=False)
            competition.save()
            return redirect('races:detail_competition', pk=competition.pk)
    return render(request, 'races/new_competition.html', {'form': form})
def new_airrace(request):
    form = AirRaceForm()
    if request.method == "POST":
        form = AirRaceForm(request.POST, request.FILES)
        if form.is_valid():
            race = form.save(commit=False)
            race.save()
            get_air_participants(race)
            return redirect('races:air_detail_race', pk=race.pk)
    return render(request, 'races/new_airrace.html', {'form': form})
def get_air_participants(race):
    onlyfiles = [f for f in os.listdir(race.folderPath) if isfile(join(race.folderPath, f))]
    raceFolderPath= "static/airraces/"+str(race.pk)
    print(raceFolderPath)
    os.mkdir(raceFolderPath)
    print(raceFolderPath)

    for kmlFile in onlyfiles:
        baseFilePath = race.folderPath + "/" + kmlFile
        finalFilePath = BASE_DIR + "/" + raceFolderPath
        print baseFilePath + "-->" + finalFilePath

        air_race_participant = AirRaceParticipant()
        air_race_participant.airrace = race
        air_race_participant.kmlpath = kmlFile
        os.system("cp %s %s" % (baseFilePath, finalFilePath))
        airParticipantName = extract_information_kml(baseFilePath)
        air_race_participant.name = airParticipantName
        air_race_participant.save()

    return HttpResponseRedirect('/air_race')
def extract_information_kml(kmlPath):
    import re  # Import the regex module.
    err_occur = []  # The list where we will store results.
    first="<td>Pilot</td><td>"
    firstv2="<td>Piloto</td><td>"
    last="</td></tr><tr><td>Takeoff</td>"
    lastv2="</td></tr><tr><td>Startplatz</td>"
    pattern = re.compile(first, re.IGNORECASE)  # Compile a case-insensitive regex pattern.
    patternv2 = re.compile(firstv2, re.IGNORECASE)  # Compile a case-insensitive regex pattern.
    with open(kmlPath, 'rt') as in_file:  # open file for reading text.
        for linenum, line in enumerate(in_file):  # Iterssate on file per line, keeping track of line numbers.
            #print line
            if pattern.search(line) != None:  # If pattern search finds a match,
                err_occur.append((linenum, line.rstrip('\n')))  # strip linebreaks, store line and line number as tuple.
                name=find_between(line,first,last)
                if name=="":
                    name = find_between(line, first, lastv2)
                return name
            elif patternv2.search(line) != None:  # If pattern search finds a match,
                err_occur.append((linenum, line.rstrip('\n')))  # strip linebreaks, store line and line number as tuple.
                name=find_between(line,first,last)
                if name=="":
                    name = find_between(line, first, lastv2)
                return name



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

def get_all_raceparticipants(race):

    participants = Participant.objects.all().filter(races=race)
    print(participants)
    return participants


#CRUD operations
def delete_task(request,competition,task):
    print "hola"
    task=Task.objects.get(pk=task)
    task.delete()
    return HttpResponseRedirect('/competitions/'+competition)
def delete_competition(request,pk):
    competition=Competition.objects.get(pk=pk)
    competition.delete()
    return HttpResponseRedirect('/competitions')
def delete_airrace(request,pk):
    race=AirRace.objects.get(pk=pk)
    baseFilePath = BASE_DIR + "/static/airraces/" + str(race.pk)
    print baseFilePath
    race.delete()
    os.system("rm -R %s" % (baseFilePath))
    return HttpResponseRedirect('/air_races')
def delete_race(request,pk):
    race=Race.objects.get(pk=pk)
    url_destination = race.type
    race.delete()
    if url_destination == 0:
        return HttpResponseRedirect('/ground_races')
    else:
        return HttpResponseRedirect('/air_races')
def edit_race(request,pk):
    race=Race.objects.get(pk=pk)
    form = RaceForm(instance=race)
    if request.method == 'POST':
        form = RaceForm(request.POST, instance=race)
        if form.is_valid():
            if race.type == 0:
                return HttpResponseRedirect('/ground_race')
            else:
                return HttpResponseRedirect('/air_race')
    return render(request, 'races/new_race.html', {'form': form})
def edit_airrace(request,pk):
    race=AirRace.objects.get(pk=pk)
    form = AirRaceForm(instance=race)
    if request.method == 'POST':
        form = AirRaceForm(request.POST, instance=race)
        if form.is_valid():
            airrace=form.save(commit=False)
            airrace.save()
            return HttpResponseRedirect('/air_races')
    return render(request, 'races/new_race.html', {'form': form})

@csrf_exempt
def create_participant(request):
    print("---------")
    #name=request.GET.get('name','')

    if request.method == 'POST':
        print("fhgjhk")
        name=request.POST.get('name','')
        image=request.POST.get('image','')
        imageFACE=request.POST.get('oe','')
        imageURL=str(image)+'&oe='+str(imageFACE)
        print(imageURL)
        pk=request.POST.get('race','')
        race = Race.objects.get(pk=pk)

        user = User()
        user.username= name
        user.first_name = name
        user.password = ''
        user.save()
        participant = Participant()
        participant.user = user
        participant.image = imageURL
        participant.save()
        create_raceparticipant(participant,race)
        raceParticipant= RaceParticipant.objects.get(participant=participant.pk,race=race.pk)
        print(raceParticipant.pk)
        get_raceparticipant(participant, race)
    return HttpResponseRedirect('/')
def create_raceparticipant(participant,race):
    raceParticipant = RaceParticipant()
    raceParticipant.participant = participant
    raceParticipant.race = race
    raceParticipant.save()
def get_raceparticipant(participant,race):
    raceParticipant= RaceParticipant.objects.get(participant=participant,race=race)
    return raceParticipant

@csrf_exempt
def create_raceposition(request):
    if request.method == 'POST':
        raceID = request.POST.get('race', '')
        race = Race.objects.get(pk=raceID)
        print("it works!!!!")

        nameID=request.POST.get('name','')
        user=User.objects.get(username=nameID)
        print(user.username)
        print("aaaaa")
        participant = Participant.objects.get(user=user)
        print(participant.user.username)
        print(participant.pk)
        print("it works!!!!")

        raceparticipant = get_raceparticipant(participant, race)
        print(raceparticipant.race)

        position = Position()
        position.instant = request.POST.get('instant', '')
        print(position.instant)
        print("it works!!!!")

        position.latitude = request.POST.get('latitude','')
        position.longitude = request.POST.get('longitude','')
        position.height = request.POST.get('height', '')
        position.raceparticipant=raceparticipant
        position.save()
        get_raceparticipant(participant,race)
    return HttpResponseRedirect('/')
def get_racepositions(raceparticipant):
    positions = Position.objects.filter(raceparticipant=raceparticipant)
    return positions
def ground_race_send(request,race, participant):
    raceparticipant = get_raceparticipant(participant,race)
    positions = get_racepositions(raceparticipant)
    print(raceparticipant.participant.user.username)
    print race
    print race.pk
    print "-----"
    #filename=create_routeparticipant_kml(positions,raceparticipant)
    write_kml_race()
    return HttpResponseRedirect('/ground_races')
def air_race_send(request,race, participant):
    #filename=create_routeparticipant_kml(positions,raceparticipant)
    participant = AirRaceParticipant.objects.get(pk=participant)
    write_kml_participant(race,participant)
    #write_kml_airrace(race)
    return HttpResponseRedirect('../..')


def send_participant(request,competition,task,participant):
    #filename=create_routeparticipant_kml(positions,raceparticipant)
    participant = CompetitionTaskParticipant.objects.get(pk=participant)

    send_single_kml(participant)

    return HttpResponseRedirect('../..')


def send_participants(request,competition,task,participant):
    participant = CompetitionTaskParticipant.objects.get(pk=participant)

    if participant.visibility == True:
        participant.visibility = False
    else:
        participant.visibility = True
    participant.save()

    competitiontaskparticipants = CompetitionTaskParticipant.objects.filter(task=task)
    competitiontaskparticipants = competitiontaskparticipants.exclude(visibility=False)

    create_kmlstxt(competitiontaskparticipants)

    return HttpResponseRedirect('../..')


#Serializers
class RaceViewSet(viewsets.ModelViewSet):
    queryset=Race.objects.all()
    serializer_class = RaceSerializer
class RaceParticipantViewSet(viewsets.ModelViewSet):
    queryset=RaceParticipant.objects.all()
    serializer_class = RaceParticipantSerializer
class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = RaceParticipantSerializer



