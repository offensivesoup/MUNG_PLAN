from django.urls import path, include
from . import views

urlpatterns = [
  path('deposit/', views.deposit_api),
]