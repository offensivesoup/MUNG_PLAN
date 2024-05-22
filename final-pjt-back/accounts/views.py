## DJANGO
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.hashers import make_password

## REST_API
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework import generics

## from pjt
from .models import Dog
from .serializers import DogListSerializer, DogSerializer, UserDetailSerializer, UserSerializer

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


## from local
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    me = request.user
    you = get_user_model().objects.get(pk = user_pk)
    if you != me:
        if me in you.followers.all():
            you.followers.remove(me)
        else:
            you.followers.add(me)
        you.save()
    return Response(status = status.HTTP_200_OK)

@api_view(['GET','POST'])
def dogs_list(request, user_pk):
    if request.method == 'GET':
        dogs = Dog.objects.filter(user = user_pk)
        serializer = DogListSerializer(dogs, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.pk == user_pk:
            serializer = DogSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE', 'PUT'])
def dog_detail(request, user_pk, dog_pk):
    dog = get_object_or_404(Dog, pk = dog_pk)
    if request.method == 'DELETE':
        if request.user.pk == user_pk:
            dog.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        if request.user.pk == user_pk:
            serializer = DogSerializer(instance=dog, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def user_detail(request, username):
    user = get_user_model().objects.get(username = username)
    serializer = UserDetailSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    serializer = UserDetailSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        if 'password' in serializer.validated_data:
            user.set_password(serializer.validated_data.pop('password'))
            user.save()
        serializer.save()
        return Response(serializer.data)