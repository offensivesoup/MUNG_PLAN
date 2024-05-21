from .models import Map, Location
from rest_framework import serializers

class MapListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('longitude','latitude',)