from rest_framework import serializers
from .models import Deposit

class DepositListSerializer(serializers.ModelSerializer):
  class Meta:
      model = Deposit
      fields = '__all__'