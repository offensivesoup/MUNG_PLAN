from django.urls import path, include
from . import views

urlpatterns = [
  # path('markets/', views.market_api)
  path('markets/', views.market_list),
  path('market/<int:product_pk>/', views.market_detail),
]