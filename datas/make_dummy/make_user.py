# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

# [참고] 현재 코드는 아래 User 모델을 기준으로 작성되어 있습니다.
"""
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
    financial_products = models.TextField(blank=True, null=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
"""


import random
import requests
import os
first_name_samples = '김이박최정강조윤장임'
middle_name_samples = '민서예지도하주윤채현지'
last_name_samples = '준윤우원호후서연아은진'


def random_name():
    result = ''
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))


# # 현재 API 에 들어있는 금융 상품 코드 리스트 저장
# DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
# SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

# API_KEY = '<API_KEY>'

# financial_products = []

# params = {
#     'auth': API_KEY,
#     # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
#     'topFinGrpNo': '020000',
#     'pageNo': 1,
# }

# 정기예금 목록 저장
# response = requests.get(DP_URL, params=params).json()
# baseList = response.get('result').get('baseList')  # 상품 목록

# for product in baseList:
#     financial_products.append(product['fin_prdt_cd'])

# # 적금 목록 저장
# response = requests.get(SP_URL, params=params).json()
# baseList = response.get('result').get('baseList')  # 상품 목록

# for product in baseList:
#     financial_products.append(product['fin_prdt_cd'])

# dict_keys = [
#     'username',
#     'gender',
#     'financial_products',
#     'age',
#     'money',
#     'salary',
# ]

# # json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

username_list = []
N = 10000
i = 0

while i < N:
    rn = random_name()
    if rn in username_list:
        continue

    username_list.append(rn)
    i += 1

import random
from datetime import datetime, timedelta



# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
import os

save_dir = 'C:/Users/SSAFY/Desktop/data2.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    for i in range(N):
        # 시작 날짜와 종료 날짜 설정 (원하는 범위 내에서 날짜를 생성할 수 있도록)
        start_date = datetime(1950, 1, 1)
        end_date = datetime(2023, 12, 31)

        # 시작 날짜와 종료 날짜 사이에서 랜덤한 날짜 생성
        random_days = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_days)

        date = random_date.strftime("%Y-%m-%d")
        user = random.randint(1,10000)

        # 1부터 10000까지 숫자 중 하나 선택
        followings = [random.randint(1, 10000)]
        phone_number = []
        while True:
            number = '010' + '-' + str(random.randint(1111,9999)) + '-' + str(random.randint(1111,9999))
            if number in phone_number:
                pass
            else:
                phone_number.append(number)
                break        
        # 랜덤한 데이터를 삽입
        file['model'] = 'accounts.User'
        file['pk'] = i + 1
        file['fields'] = {
            # 랜덤한 0~5개의 상품을 가입하도록 삽입됨 
            'password': '1234',
            "last_login": "2024-05-16T23:39:26.445Z",
            'is_superuser': False,
            'username': username_list[i],  # 유저 이름 랜덤 생성
            "first_name":username_list[i][0],
            "last_name" :username_list[i][1:],
            'email' : 'abc@naver.com',
            'is_staff': False,
            'is_active': True,
            "date_joined": "2024-05-16T02:24:30.706Z",
            'nickname': username_list[i],
            'phone_number' : number,
            "address" : address,
            "profile_img": "profile_images/default.png",
            "birth_date": date,
            "groups": [],
            "user_permissions": [],
            'followings': followings,
        }

        json.dump(file, f, ensure_ascii=False, indent='\t')
        if i != N - 1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')