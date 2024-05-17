from rest_framework import serializers
from .models import Deposit

class DepositListSerializer(serializers.ModelSerializer):
  class Meta:
      model = Deposit
      fields = '__all__'
      
class DepositSerializer(serializers.ModelSerializer):
  like_count = serializers.IntegerField(source='like_users.count', read_only=True)
  class Meta:
    model = Deposit
    fields = '__all__'