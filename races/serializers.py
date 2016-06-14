from .models import Race
from rest_framework import serializers,pagination

class RaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        resource_name = 'race'