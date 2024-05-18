from rest_framework import serializers
from .models import Market


class MarketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        # fields = ('id', 'state', 'img', 'kind', 'gender', 'notice', 'center_address')
        fields = '__all__'


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'