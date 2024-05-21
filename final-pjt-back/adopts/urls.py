from django.urls import path, include
from . import views

urlpatterns = [
  # path('adopt/', views.adopt_api)
  path('adopts/', views.adopt_list),
  path('adopt/<int:adopt_pk>/', views.adopt_detail),
  path('adopt/filter/<str:category>/', views.adopt_filtering),
]