## django
from django.shortcuts import render
from django.http import JsonResponse

## DRF
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

## from pjt
from .models import Deposit

## library
import os
import requests
from datetime import datetime
import html

# Create your views here.
@api_view(['GET'])
def deposit_api(request):
    return
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
