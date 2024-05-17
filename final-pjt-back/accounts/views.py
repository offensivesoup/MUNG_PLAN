## DJANGO
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
## REST_API
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
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
    return Response(status = status.HTTP_200_OK)