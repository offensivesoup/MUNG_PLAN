## django
from django.shortcuts import render
from django.http import JsonResponse

## DRF
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

## from pjt
from .models import Market

## library
import os
import requests
from datetime import datetime
import html
import re
## 네이버 쇼핑 api가져오기
@api_view(['GET'])
def market_api(request):
    records = Market.objects.all()
    for record in records:
        cleaned_title = re.sub('<b>|</b>', '', record.item_name)
        record.item_name = cleaned_title
        record.save()
    return JsonResponse(records.json())
#   ## 기본 정보들
#   url = 'https://openapi.naver.com/v1/search/shop.json'
#   NAVER_ID = os.getenv('NAVER_ID')
#   NAVER_KEY = os.getenv('NAVER_KEY')
#   headers = {'X-Naver-Client-Id' : NAVER_ID , 'X-Naver-Client-Secret' : NAVER_KEY}
#   ## 네이버 애견 검색 카테고리에 있는 단어들 추려왔다
#   serach_words = ['영양제', '계단', '장난감', '매트', '수제간식', '샴푸', '배변패드', '크리너', '노즈워크', '침대/해먹']
#   ## 그럼 해당 단어들을 돌면서 파라미터 값에 넣어준다
#   for word in serach_words:
#     ## word 당 1000개의 데이터를 확보하기로 했으니 100개짜리 데이터를 10번씩 불러온다
#     for i in range(1,11):
#       ## 파라미터 값 (가이드 참고)
#       params = {
#         'query' : f'강아지 {word}',
#         'display' : 100,
#         'start' : i
#       }
#       ## 네이버는 API_KEY가 아니라, 클라이언트 아이디와 키를 헤더에, 나머지를 파라미터에 구분지어 넣는다
#       response = requests.get(url, headers=headers, params=params)
#       ## 해당 데이터의 응답이 성공했다면
#       if response.status_code == 200:
#         ## 데이터를 json으로 변환
#         response_data = response.json()  # Convert response content to JSON
#         for item in response_data.get('items', []):
#           ## 인스턴스 생성하고, 모델에각 필드값에 설계했던 값을 지정해주는 작엄
#           market = Market()
#           market.item_name = html.unescape(item.get('title', 'No Title'))
#           market.item_img = item.get('image', 'No Image')
#           item_low_price = item.get('lprice', 0)
#           market.item_low_price = int(item_low_price) if item_low_price else 0
#           item_high_price = item.get('hprice', 0)
#           market.item_high_price = int(item_high_price) if item_high_price else 0 
#           market.item_seller = item.get('mallName', 'No Seller')
#           market.item_brand = item.get('brand', 'No Brand')
#           market.item_maker = item.get('maker', 'No Maker')
#           market.item_link = item.get('link', 'No Link')
#           market.item_type = f'강아지 {params["query"]}'
#           market.item_cateogry_1 = item.get('category1', 'No Category 1')
#           market.item_cateogry_2 = item.get('category2', 'No Category 2')
#           market.item_cateogry_3 = item.get('category3', 'No Category 3')

#           market.save()
#       ## 한 사이클이 돌면 출력해줄 멘트
#       print('정상저장')
#   return JsonResponse(response_data, safe=False)  # Return the JSON data