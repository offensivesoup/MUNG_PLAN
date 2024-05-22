## DJANGO
from django.shortcuts import get_object_or_404, get_list_or_404

## REST_API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

## from local
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

## article
@api_view(['GET'])
def article_list(request):
  articles = get_list_or_404(Article)
  serializer = ArticleListSerializer(articles, many=True)
  return Response(serializer.data)

# create할 때만 로그인이 필요하도록 나눔
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
  serializer = ArticleSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)

## 커뮤니티 글 분류
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def article_filtering(request, category_name):
  articles = Article.objects.filter(category = category_name)
  serializer = ArticleListSerializer(articles, many = True)
  print(serializer.data)
  return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
      serializer = ArticleSerializer(article)
      return Response(serializer.data)
    elif request.method == 'DELETE':
      article.delete()
      return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
      serializer = ArticleSerializer(instance = article, data = request.data, partial = True)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_200_OK)
      return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)

## comment

@api_view(['GET'])
def comment_list(request, article_pk):
    comments = get_list_or_404(Comment.objects.filter(article_id = article_pk))
    serializer = CommentSerializer(comments, many = True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
      serializer = CommentSerializer(comment)
      return Response(serializer.data)
    elif request.method == 'DELETE':
      comment.delete()
      return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
      serializer = CommentSerializer(comment, data = request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(article = article, user = request.user)
      return Response(serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user in article.like_users.all():
      article.like_users.remove(request.user)
    else:
      article.like_users.add(request.user)
    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
def isliked(request, article_pk):
   article = Article.objects.get(pk=article_pk)
   if request.user in article.like_users.all():
      return Response(status=status.HTTP_200_OK)
   else:
      return Response(status=status.HTTP_400_BAD_REQUEST)