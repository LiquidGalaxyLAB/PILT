from django import forms
import models

class RaceForm(forms.ModelForm):
    class Meta:
        model = models.Race
        exclude=[]