## DJANGO
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.conf import settings

## REST_API
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
## from pjt
from .models import Dog
from .serializers import DogListSerializer, DogSerializer, UserDetailSerializer

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

## from local
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    me = request.user.pk
    you = get_user_model().objects.get(pk = user_pk)
    if you != me:
        if me in you.followers.all():
            you.followers.remove(me)
        else:
            you.followers.add(me)
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
    