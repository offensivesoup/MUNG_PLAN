from rest_framework import serializers
from .models import Market


class MarketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'item_img', 'item_name')


# class MarketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Market
#         fields = '__all__'