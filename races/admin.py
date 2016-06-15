from django.contrib import admin
from .models import Race,Participant,RaceParticipant
# Register your models here.


admin.site.register(Race)
admin.site.register(Participant)
admin.site.register(RaceParticipant)