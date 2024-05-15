## django
from django.shortcuts import render
from django.http import JsonResponse

## DRF
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

## from pjt
from .models import Map

## library
import os
import requests
from datetime import datetime
import html


# Create your views here.
def maps_api(request):
    return
    # url = 'https://api.odcloud.kr/api/15111389/v1/uddi:41944402-8249-4e45-9e9d-a52d0a7db1cc'
    # MAP_KEY = os.getenv('MAP_KEY')
    # for i in range(1,25):
    #     params = {
    #         'page' : i,
    #         'perPage' : 1000,
    #         'serviceKey' : MAP_KEY,
    #     }
    #     response = requests.get(url, params=params)
    #     if response.status_code == 200:
    #         response_data = response.json()
    #         for item in response_data['data']:
    #             map = Map()
    #             map.facility_name = item.get('시설명', '없음')
    #             map.facility_explain = item.get('기본 정보_장소설명', '없음')
    #             map.facility_parking = item.get('주차 가능여부', '없음')
    #             map.facility_province = item.get('시도 명칭', '없음')
    #             map.facility_location = item.get('시군구 명칭', '없음')
    #             map.facility_lat = item.get('위도', 0)
    #             map.facility_lng = item.get('경도', 0)
    #             map.facility_new_address = item.get('도로명주소', '없음')
    #             map.facility_old_address = item.get('지번주소', '없음')
    #             map.facility_holiday = item.get('휴무일', '없음')
    #             map.facility_category1 = item.get('카테고리1', '없음')
    #             map.facility_category2 = item.get('카테고리2', '없음')
    #             map.facility_category3 = item.get('카테고리3', '없음')
    #             map.facility_link = item.get('홈페이지', '없음')
    #             map.save()
    #         print(f'{i}번 가져옴')
    # return JsonResponse(response_data)