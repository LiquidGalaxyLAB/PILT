from django.shortcuts import render
from django.http import HttpResponse
from .forms import RaceForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


# Create your views here.

def airview(request):
    return render(request,'races/air_race.html', {})

def groundview(request):
    return render(request,'races/ground_race.html', {})

def detail_race(request):
    race = get_object_or_404(Race, pk=pk)
    return render(request, 'races/detail_race.html', {'post': race})


def new_race(request):
    if request.method == "POST":
        form = RaceForm(request.POST)
        if form.is_valid():
            race = form.save(commit=False)
            race.save()
            return redirect('race.views.race_detail', pk=race.pk)
    else:
        form = RaceForm()
        return render(request, 'races/new_race.html', {'form': form})



