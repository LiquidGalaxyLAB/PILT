from django.contrib.auth import get_user_model

from .models import Race,Participant,RaceParticipant
from rest_framework import serializers,pagination

class RaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        resource_name = 'race'

class RaceParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceParticipant

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
