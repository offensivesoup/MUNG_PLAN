from django.urls import path, include
from . import views

urlpatterns = [
  # 여러 개(리스트) 출력하는 건 s를 붙이는 것으로 url 수정
  path('deposits/', views.deposit_list),
  path('deposit/<int:deposit_pk>/', views.deposit_detail),
  path('deposit/<int:deposit_pk>/likes/', views.deposit_likes),
  path('deposits/recommend/<int:user_id>/', views.deposit_recommend),
  path('insurances/', views.insurance_list),
]