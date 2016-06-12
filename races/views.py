from django.shortcuts import render
from django.http import HttpResponseRedirect

from races.models import Race
from .forms import RaceForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404



# Create your views here.

def airview(request):
    return render(request,'races/air_race.html', {})

def groundview(request):
    races=Race.objects.all()
    return render(request,'races/ground_race.html',{'races':races})


def detail_race(request,pk):
    race = get_object_or_404(Race, pk=pk)
    return render(request, 'races/detail_race.html', {'race': race})


def new_race(request):
    form = RaceForm()
    if request.method == "POST":
        form = RaceForm(request.POST, request.FILES)
        if form.is_valid():
            race = form.save(commit=False)
            race.save()
            return redirect('detail_race', pk=race.pk)
    return render(request, 'races/new_race.html', {'form': form})


def delete_race(request,pk):
    race=Race.objects.get(pk=pk).delete()
    if race.type == 0:
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
