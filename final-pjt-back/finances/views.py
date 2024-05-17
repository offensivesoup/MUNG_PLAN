## django
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
## DRF
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
## from pjt
from .models import Deposit
from .serializer import DepositListSerializer, DepositSerializer
## library
import os
import requests
from datetime import datetime
import random

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
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def deposit_detail(request, deposit_pk):
    deposit = get_object_or_404(Deposit, pk = deposit_pk)
    serializer = DepositSerializer(deposit)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['POST'])
def deposit_likes(request, deposit_pk):
    deposit = get_object_or_404(Deposit, pk=deposit_pk)
    if request.user in deposit.like_users.all():
        deposit.like_users.remove(request.user)
    else:
        deposit.like_users.add(request.user)
    return Response(status = status.HTTP_200_OK)

# Create your views here.
@api_view(['GET'])
def deposit_recommend(request):
    ## 강아지를 키우고 있따면
    deposit = Deposit.objects.all()
    
    return
