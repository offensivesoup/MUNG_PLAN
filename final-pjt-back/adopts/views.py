## django
from django.shortcuts import render
from django.http import JsonResponse

## DRF
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

## from pjt
from .models import Adopt

## library
import os
import requests
from datetime import datetime

# 유기견 데이터 불러오기
@api_view(['GET'])
def adopt_api(request):
  if request.method == 'GET':
    return
    ## 총 6452 개의 데이터를 가져옴
    # for i in range(1, 8):
    #   url = 'https://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic'
    #   ADOPT_KEY = os.getenv('ADOPT_KEY')
    #   ## 유기견 총 
    #   params ={'serviceKey' : ADOPT_KEY,'upkind' : 417000, 'pageNo' : i, 'numOfRows' : 1000, '_type' : 'json'}
    #   response = requests.get(url, params=params)
    #   data = response.json()
    #   for item in data['response']['body']['items']['item']:
    #     adopt = Adopt()
    #     adopt.start_date = datetime.strptime(item.get('noticeSdt'), '%Y%m%d').date()
    #     adopt.end_date = datetime.strptime(item.get('noticeEdt'),  '%Y%m%d').date()
    #     adopt.state = item.get('processState')
    #     adopt.img = item.get('popfile')
    #     adopt.gender = item.get('sexCd')
    #     adopt.notice = item.get('specialMark')
    #     adopt.kind = item.get('kindCd')
    #     adopt.center_name = item.get('careNm')
    #     adopt.center_telephone = item.get('careTel')
    #     adopt.center_address = item.get('careAddr')
    #     adopt.save()
    # return JsonResponse({'status': 'success', 'message': 'Data imported successfully'}, status=200)
        
