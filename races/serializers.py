from .models import Race
from rest_framework import serializers

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('name','type','image','localization_name','initial_date','initial_time')