from django.urls import path, include
from . import views

urlpatterns = [
  # for article
  path('articles/', views.article_list),
  path('articles/<str:category_name>/', views.article_filtering),
  path('article/<int:article_pk>/', views.article_detail),
  # for comments
  path('comments/', views.comment_list),
  path('comments/<int:comment_pk>/', views.comment_detail),
  path('<int:article_pk>/comments/', views.comment_create),
  path('<int:article_pk>/likes/', views.likes),
]

