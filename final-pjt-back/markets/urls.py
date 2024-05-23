from django.urls import path, include
from . import views

urlpatterns = [
  # path('markets/', views.market_api)
  path('markets/', views.market_list),
  path('markets/product/<str:category_name>/', views.product_filter)
  # path('market/<int:product_pk>/', views.market_detail),
]