## django
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.conf import settings

## DRF
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

## from pjt
from .models import Deposit, Insurance
from accounts.models import Dog
from .serializers import DepositListSerializer, DepositSerializer, InsuranceListSerializer

## library
import os
import requests
from datetime import datetime
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ## 예금, 적금 가져오기
# url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
# API_KEY = os.getenv('FINANCE_KEY')
# params = {
#     'auth' : API_KEY,
#     'topFinGrpNo' : '030300',
#     'pageNo' : 3
# }
# response = requests.get(url, params=params)
# if response.status_code == 200:
#     data = response.json()
#     for item in data['result']['baseList']:
#         deposit = Deposit()
#         deposit.category = '저축은행적금'
#         deposit.product_num = item.get('fin_prdt_cd')
#         deposit.company_name = item.get('kor_co_nm')
#         deposit.product_name = item.get('fin_prdt_nm')
#         deposit.product_explain = item.get('mtrt_int')
#         deposit.special_explain = item.get('etc_note')
#         deposit.special_condition = item.get('spcl_cnd')
#         deposit.join_member = item.get('join_member')
#         deposit.limit = item.get('max_limit')
#         for option in data['result']['optionList']:
#             if option['fin_prdt_cd'] == deposit.product_num:
#                 deposit.save_term = option.get('save_trm')
#                 deposit.interate_type = option.get('intr_rate_type_nm')
#                 deposit.interate_rate = option.get('intr_rate')
#                 deposit.maxi_interate_rate = option.get('intr_rate2')
#                 deposit.save()
#     print('저장')
# return JsonResponse(data)
@api_view(['GET'])
def deposit_list(request):
    deposits = get_list_or_404(Deposit)
    serializer = DepositListSerializer(deposits, many = True)
    return Response({'static_url': settings.STATIC_URL, 'deposits': serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def deposit_detail(request, deposit_pk):
    deposit = get_object_or_404(Deposit, pk = deposit_pk)
    serializer = DepositSerializer(deposit)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_likes(request, deposit_pk):
    deposit = get_object_or_404(Deposit, pk=deposit_pk)
    if request.user in deposit.like_users.all():
        deposit.like_users.remove(request.user)
    else:
        deposit.like_users.add(request.user)
    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def deposit_recommend(request, user_id):
    User = get_user_model()
    users = User.objects.all()
    user = get_object_or_404(User, id=user_id)
    liked_deposits = user.like_deposit.select_related('category').all()
    deposits = Deposit.objects.all()
    user_dogs = Dog.objects.filter(user=user).prefetch_related('breed').all()
    
    if not users.exists() or not deposits.exists():
        return Response({"error": "No users or deposits found"}, status=400)

    # Create mappings for user IDs and deposit IDs
    user_ids = {user.id: idx for idx, user in enumerate(users)}
    deposit_ids = {deposit.id: idx for idx, deposit in enumerate(deposits)}

    # Extract user demographic information
    # Assuming User model has fields: age, gender, and location
    user_info_matrix = np.array([
        [int(datetime.now().year-user.birth_date.year)]
        for user in users
    ])

    # Normalize the user_info_matrix
    user_info_matrix = (user_info_matrix - user_info_matrix.mean(axis=0)) / user_info_matrix.std(axis=0)
    
    # Initialize user_likes_matrix
    user_likes_matrix = np.zeros((len(users), len(deposits)))
    for deposit in deposits:
        for user in deposit.like_users.all():
            user_idx = user_ids.get(user.id)
            deposit_idx = deposit_ids.get(deposit.id)
            if user_idx is not None and deposit_idx is not None:
                user_likes_matrix[user_idx, deposit_idx] = 1

    print("User Likes Matrix:")
    print(user_likes_matrix)

    # Initialize user_dog_matrix
    user_dog_matrix = np.zeros((len(users), 1))
    for dog in user_dogs:
        user_idx = user_ids.get(dog.user.id)
        if user_idx is not None:
            user_dog_matrix[user_idx, 0] = 1

    print("User Dog Matrix:")
    print(user_dog_matrix)

    # Combine the matrices based on available data
    if user_dogs.exists() and liked_deposits.exists():
        combined_matrix = np.hstack((user_likes_matrix, user_dog_matrix, user_info_matrix))
    elif user_dogs.exists():
        combined_matrix = np.hstack((np.zeros((len(users), len(deposits))), user_dog_matrix, user_info_matrix))
    elif liked_deposits.exists():
        combined_matrix = np.hstack((user_likes_matrix, np.zeros((len(users), 1)), user_info_matrix))
    else:
        combined_matrix = user_info_matrix

    print("Combined Matrix:")
    print(combined_matrix)
    
    # Calculate the cosine similarity matrix
    similarity_matrix = cosine_similarity(combined_matrix)
    target_user_index = user_ids[user_id]
    
    # Calculate similarities of the target user to all other users
    user_similarities = similarity_matrix[target_user_index]
    print("User Similarities:")
    print(user_similarities)

    # Generate recommendations based on similar users
    recommended_deposits = []
    deposit_list = list(deposits)
    for user_idx, similarity in enumerate(user_similarities):
        if user_idx != target_user_index and similarity > 0:
            liked_deposits_indices = np.where(user_likes_matrix[user_idx] == 1)[0]
            for deposit_idx in liked_deposits_indices:
                if user_likes_matrix[target_user_index, deposit_idx] == 0:
                    recommended_deposits.append((deposit_list[deposit_idx], similarity))

    # Sort the recommendations by similarity and select top 10
    recommended_deposits.sort(key=lambda x: x[1], reverse=True)
    top_recommended_deposits = [deposit for deposit, similarity in recommended_deposits[:10]]
    
    # Serialize the recommended deposits
    response_data = [{
        'id': deposit.id,
        'category': deposit.category if deposit.category else None,
        'company_name': deposit.company_name,
        'product_num': deposit.product_num,
        'product_name': deposit.product_name,
        'product_explain': deposit.product_explain,
        'special_explain': deposit.special_explain,
        'special_condition': deposit.special_condition,
        'join_member': deposit.join_member,
        'limit': deposit.limit,
        'save_term': deposit.save_term,
        'interate_type': deposit.interate_type,
        'interate_rate': deposit.interate_rate,
        'maxi_interate_rate': deposit.maxi_interate_rate,
        'link' : deposit.link,
        'img' : deposit.company_image
    } for deposit in top_recommended_deposits]

    print(response_data)

    return Response(response_data)

## 보험 관련
@api_view(['GET'])
def insurance_list(request):
    insurances = Insurance.objects.all()
    serializer = InsuranceListSerializer(insurances, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)