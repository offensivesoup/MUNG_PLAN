from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import authenticate
from .models import Dog

UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
      required=True,
      allow_blank=False,
      max_length=255
    )
    phone_number = serializers.CharField(
      required=True,
      allow_blank=False,
      max_length=255
    )
    address = serializers.CharField(
      required=True,
      allow_blank=False,
      max_length=255
    )
    profile_img = serializers.ImageField(
      required=True,
    )
    birth_date = serializers.DateField(
      required=True,
    )
    first_name = serializers.CharField(
      required=True,
      allow_blank=False,
      max_length=10
    )
    last_name = serializers.CharField(
      required=True,
      allow_blank=False,
      max_length=10
    )
        
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'last_name' : self.validated_data.get('last_name',''),
            'first_name' : self.validated_data.get('first_name', ''),
            'email' : self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'phone_number' : self.validated_data.get('phone_number', ''),
            'address' : self.validated_data.get('address', ''),
            'profile_img' : self.validated_data.get('profile_img', ''),
            'birth_date' : self.validated_data.get('birth_date', '')
        }
        
class CustomUserDetailsSerializer(UserDetailsSerializer):
  class Meta:
      extra_fields = []
      # see https://github.com/iMerica/dj-rest-auth/issues/181
      # UserModel.XYZ causing attribute error while importing other
      # classes from `serializers.py`. So, we need to check whether the auth model has
      # the attribute or not
      if hasattr(UserModel, 'USERNAME_FIELD'):
          extra_fields.append(UserModel.USERNAME_FIELD)
      if hasattr(UserModel, 'EMAIL_FIELD'):
          extra_fields.append(UserModel.EMAIL_FIELD)
      if hasattr(UserModel, 'first_name'):
          extra_fields.append('first_name')
      if hasattr(UserModel, 'last_name'):
          extra_fields.append('last_name')
      if hasattr(UserModel, 'nickname'):
          extra_fields.append('nickname')    
      if hasattr(UserModel, 'phone_number'):
          extra_fields.append('phone_number')    
      if hasattr(UserModel, 'address'):
          extra_fields.append('address')    
      if hasattr(UserModel, 'profile_img'):
          extra_fields.append('profile_img')
      if hasattr(UserModel, 'birth_date'):
          extra_fields.append('birth_date')
      model = UserModel
      fields = ('pk', *extra_fields)
      read_only_fields = ('email',)
      
class CustomLoginSerializer(LoginSerializer):
  username = serializers.CharField(required=True)
  password = serializers.CharField(required=True, write_only=True)

class DogListSerializer(serializers.ModelSerializer):
    class Meta:
      model = Dog
      fields = '__all__'
    
    
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'
        read_only_fields = ('user',)
