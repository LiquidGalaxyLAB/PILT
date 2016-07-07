from django.contrib import admin
from .models import Race,Participant,RaceParticipant,Position, AirRace, AirRaceParticipant, Competition, Task

# Register your models here.


admin.site.register(Race)
admin.site.register(Participant)
admin.site.register(RaceParticipant)
admin.site.register(Position)
admin.site.register(AirRace)
admin.site.register(AirRaceParticipant)
admin.site.register(Competition)
admin.site.register(Task)