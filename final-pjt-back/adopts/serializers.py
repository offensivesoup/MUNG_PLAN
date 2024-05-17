from rest_framework import serializers
from .models import Adopt


class AdoptListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopt
        # fields = ('id', 'state', 'img', 'kind', 'gender', 'notice', 'center_address')
        fields = '__all__'


class AdoptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopt
        fields = '__all__'