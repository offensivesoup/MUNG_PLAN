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

## 네이버 쇼핑 api가져오기
def market_api(request):
  MAP_ID = os.getenv('MAP_ID')
  MAP_KEY = os.getenv('MAP_KEY')
  headers = {'X-Naver-Client-Id' : {MAP_ID} , 'X-Naver-Client-Secret' : {MAP_KEY}}
  return
  