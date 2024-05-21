from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user_nickname')

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'user')

    def get_user_nickname(self, obj):
        return obj.user.nickname

class ArticleSerializer(serializers.ModelSerializer):
  class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comment
      fields = ('id', 'content', 'user')  
  
  comment_set = CommentDetailSerializer(many = True, read_only = True)
  comment_count = serializers.IntegerField(source='comment_set.count', read_only = True)
  
  class Meta:
      model = Article
      fields = '__all__'
      read_only_fields = ('user','like_users')

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
      model = Comment
      fields = '__all__'
      read_only_fields = ('article', 'user',)