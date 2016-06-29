from django import forms
import models

class RaceForm(forms.ModelForm):
    latitude = forms.CharField(widget=forms.TextInput(attrs={'id': 'latitudeMaps'}));
    longitude = forms.CharField(widget=forms.TextInput(attrs={'id': 'longitudeMaps'}));
    localization_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'localization_nameMaps'}));
    initial_date = forms.CharField(widget=forms.TextInput(attrs={'class':'datepicker'}))

    initial_date
    class Meta:
        model = models.Race
        exclude=[]


class AirRaceForm(forms.ModelForm):
    class Meta:
        model = models.AirRace
        exclude = []