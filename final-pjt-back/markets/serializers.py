from rest_framework import serializers
from .models import Market


class MarketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'item_img', 'item_name', 'item_low_price')


# class MarketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Market
#         fields = '__all__'