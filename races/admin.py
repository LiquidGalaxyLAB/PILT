from django.contrib import admin
from .models import Race,Participant,RaceParticipant,Position, AirRace, AirRaceParticipant

# Register your models here.


admin.site.register(Race)
admin.site.register(Participant)
admin.site.register(RaceParticipant)
admin.site.register(Position)
admin.site.register(AirRace)
admin.site.register(AirRaceParticipant)
