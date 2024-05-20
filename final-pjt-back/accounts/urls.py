from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_pk>/follow/', views.follow),
    path('<int:user_pk>/dogs/', views.dogs_list),
    path('<int:user_pk>/dogs/<int:dog_pk>/', views.dog_detail),
    path('detail/<str:username>/', views.user_detail)
]
