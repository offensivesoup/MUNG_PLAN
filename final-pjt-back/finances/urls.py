from django.urls import path, include
from . import views

urlpatterns = [
  path('deposit/', views.deposit_list),
  path('deposit/<int:deposit_pk>/', views.deposit_detail),
  path('deposit/<int:deposit_pk>/likes', views.deposit_likes),
  path('deposit/recommend', views.deposit_recommend),
]