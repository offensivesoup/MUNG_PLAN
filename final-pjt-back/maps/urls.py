from django.urls import path, include
from . import views

urlpatterns = [
  path('maps/<str:category_name>/<str:latitude>/<str:longitude>', views.maps_api),
  path('maps/<str:region>/', views.maps_search)
]