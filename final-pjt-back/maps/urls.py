from django.urls import path, include
from . import views

urlpatterns = [
  path('maps/', views.maps_api)
]